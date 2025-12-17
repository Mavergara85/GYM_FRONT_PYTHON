from datetime import datetime

from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    session,
)
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# ---------- Configuración básica ----------
app.config["SECRET_KEY"] = "cambia-esta-clave-secreta"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///wellness_center.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


# ---------- Modelos de base de datos ----------
class Plan(db.Model):
    __tablename__ = "plan"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    descripcion = db.Column(db.String(255))
    usuarios = db.relationship("Usuario", back_populates="plan")

    def __repr__(self):
        return f"<Plan {self.nombre}>"


class Usuario(db.Model):
    __tablename__ = "usuario"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    creado_en = db.Column(db.DateTime, default=datetime.utcnow)

    plan_id = db.Column(db.Integer, db.ForeignKey("plan.id"))
    plan = db.relationship("Plan", back_populates="usuarios")

    perfil = db.relationship("Perfil", back_populates="usuario", uselist=False)

    def __repr__(self):
        return f"<Usuario {self.email}>"


class Perfil(db.Model):
    __tablename__ = "perfil"

    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuario.id"))
    altura_cm = db.Column(db.Float)
    peso_kg = db.Column(db.Float)
    objetivo = db.Column(db.String(255))

    usuario = db.relationship("Usuario", back_populates="perfil")

    def __repr__(self):
        return f"<Perfil usuario_id={self.usuario_id}>"


# ---------- Rutas ----------


@app.route("/", methods=["GET"])
def index():
    planes = Plan.query.all()
    usuario_actual = None
    if "usuario_id" in session:
        usuario_actual = Usuario.query.get(session["usuario_id"])

    return render_template("index.html", planes=planes, usuario=usuario_actual)


@app.route("/registrar", methods=["POST"])
def registrar():
    nombre = (request.form.get("nombre") or "").strip()
    email = (request.form.get("email") or "").strip().lower()
    password = request.form.get("password")
    plan_id = request.form.get("plan_id")
    objetivo = (request.form.get("objetivo") or "").strip()

    if not (nombre and email and password and plan_id):
        flash("Por favor completa todos los campos obligatorios.", "error")
        return redirect(url_for("index"))

    existente = Usuario.query.filter_by(email=email).first()
    if existente:
        flash("Ya existe una cuenta con ese email. Inicia sesión.", "error")
        return redirect(url_for("index"))

    password_hash = generate_password_hash(password)

    usuario = Usuario(
        nombre=nombre,
        email=email,
        password_hash=password_hash,
        plan_id=int(plan_id),
    )
    db.session.add(usuario)
    db.session.commit()

    if objetivo:
        perfil = Perfil(usuario_id=usuario.id, objetivo=objetivo)
        db.session.add(perfil)
        db.session.commit()

    session["usuario_id"] = usuario.id
    flash("Registro exitoso. Bienvenido a Wellness Center.", "success")
    return redirect(url_for("index"))


@app.route("/login", methods=["POST"])
def login():
    email = (request.form.get("login_email") or "").strip().lower()
    password = request.form.get("login_password")

    usuario = Usuario.query.filter_by(email=email).first()

    if not usuario or not check_password_hash(usuario.password_hash, password):
        flash("Email o contraseña incorrectos.", "error")
        return redirect(url_for("index"))

    session["usuario_id"] = usuario.id
    flash("Has iniciado sesión correctamente.", "success")
    return redirect(url_for("index"))


@app.route("/logout", methods=["POST"])
def logout():
    session.pop("usuario_id", None)
    flash("Sesión cerrada correctamente.", "success")
    return redirect(url_for("index"))


# ---------- Utilidades de inicialización ----------


def crear_bd_y_planes():
    with app.app_context():
        db.create_all()

        if Plan.query.count() == 0:
            planes_iniciales = [
                Plan(
                    nombre="Yoga Zen",
                    precio=35.0,
                    descripcion="Sesiones suaves para equilibrio cuerpo‑mente.",
                ),
                Plan(
                    nombre="Power Lift",
                    precio=45.0,
                    descripcion="Fuerza, potencia y entrenamiento funcional.",
                ),
                Plan(
                    nombre="Wellness Total",
                    precio=55.0,
                    descripcion="Cardio, fuerza y mindfulness en un solo plan.",
                ),
            ]
            db.session.add_all(planes_iniciales)
            db.session.commit()


crear_bd_y_planes()

if __name__ == "__main__":
    app.run(debug=True)
