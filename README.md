# Wellness Center

## Descripción
Wellness Center es una aplicación web desarrollada con Flask que permite a los usuarios registrarse, iniciar sesión y gestionar sus perfiles en un centro de bienestar. La aplicación incluye planes de suscripción y perfiles de usuario, utilizando una base de datos SQLite con SQLAlchemy para el manejo de datos.

## Tecnologías Utilizadas
- **Backend**: Flask (Python)
- **Base de Datos**: SQLite con SQLAlchemy ORM
- **Frontend**: Jinja2 templates, Tailwind CSS
- **Autenticación**: Sesiones con Werkzeug
- **Estilos**: CSS personalizado con Tailwind

## Estructura del Proyecto
```
wellness_center/
├── app.py                 # Archivo principal de la aplicación Flask
├── instance/              # Carpeta para la base de datos SQLite
├── static/
│   └── style.css          # Estilos CSS personalizados
└── templates/
    └── index.html         # Plantilla principal de la interfaz
```

## Instalación y Configuración

### Paso 1: Clonar el Repositorio
```bash
git clone https://github.com/tu-usuario/wellness-center.git
cd wellness-center
```

### Paso 2: Crear un Entorno Virtual
```bash
python -m venv venv
```

### Paso 3: Activar el Entorno Virtual
- En Windows:
  ```bash
  venv\Scripts\activate
  ```
- En macOS/Linux:
  ```bash
  source venv/bin/activate
  ```

### Paso 4: Instalar Dependencias
```bash
pip install flask flask-sqlalchemy werkzeug
```

### Paso 5: Ejecutar la Aplicación
```bash
python app.py
```
La aplicación se ejecutará en `http://127.0.0.1:5000/` con modo debug activado.

## Uso de la Aplicación

### Registro de Usuario
1. Ve a la página principal.
2. Completa el formulario de registro con tu nombre, email y contraseña.
3. Opcionalmente, selecciona un plan de bienestar.
4. Haz clic en "Registrarse".

### Inicio de Sesión
1. Usa el formulario de login con tu email y contraseña.
2. Serás redirigido a la página principal con tu sesión iniciada.

### Gestión de Perfil
- Una vez logueado, puedes ver y editar tu perfil.
- Los perfiles están vinculados a usuarios y planes.

## Base de Datos
- La base de datos se crea automáticamente al ejecutar la aplicación.
- Modelos principales:
  - **Usuario**: Información del usuario (email, contraseña hasheada).
  - **Perfil**: Detalles adicionales del usuario.
  - **Plan**: Planes de suscripción disponibles.

## Desarrollo
- Para modificar planes iniciales, edita la función `crear_bd_y_planes()` en `app.py`.
- Asegúrate de que los emails estén en minúsculas y sin espacios.
- Usa `flash()` para mensajes de error o éxito.

## Contribución
1. Fork el proyecto.
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`).
3. Commit tus cambios (`git commit -am 'Agrega nueva funcionalidad'`).
4. Push a la rama (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request.

## Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.