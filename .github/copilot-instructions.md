# AI Coding Guidelines for Wellness Center

## Architecture Overview
- **Flask Web App**: Single-file `app.py` with routes, models, and initialization.
- **Database**: SQLite with SQLAlchemy ORM. Models: `Plan` (plans), `Usuario` (users), `Perfil` (profiles) with bidirectional relationships (e.g., `Usuario.plan` and `Plan.usuarios`).
- **Frontend**: Single-page Jinja2 template in `templates/index.html` with sections for hero, plans display, registration, and login forms. Static CSS in `static/style.css`. Uses Tailwind CSS via CDN with custom theme colors (wcDark, wcLight, wcAccent) configured in `<script>` tag.
- **Authentication**: Session-based with Werkzeug password hashing. Flash messages for feedback.

## Key Patterns
- **Models**: Use `db.relationship` for bidirectional links (e.g., `Usuario.plan` and `Plan.usuarios`, `Usuario.perfil` and `Perfil.usuario`).
- **Routes**: POST for actions (register, login, logout), GET for index. Validate inputs, use `flash()` for messages, redirect on errors. Strip and lower emails, check for duplicates.
- **Database Ops**: Always in `app.app_context()`. Initialize with `db.create_all()` and seed data in `crear_bd_y_planes()`.
- **Language**: Spanish for UI, comments, and data. Use lowercase emails, strip/validate inputs.
- **Styling**: Custom Tailwind config in `<script>` tag. Focus on minimal, modern design with custom CSS classes.

## Workflows
- **Run App**: `python app.py` (debug=True). Database auto-creates at `wellness_center.db`.
- **Add Plans**: Modify `planes_iniciales` list in `crear_bd_y_planes()`.
- **User Flow**: Register → creates Usuario + optional Perfil → session set → redirect to index.

## Conventions
- **Imports**: Group Flask imports, then SQLAlchemy, then utilities.
- **Config**: Hardcoded secrets (change in production). Track modifications off.
- **Error Handling**: Check existence (e.g., duplicate email), flash errors, redirect.
- **Timestamps**: `datetime.utcnow` for `creado_en`.

Reference: [app.py](app.py) for models/routes, [templates/index.html](templates/index.html) for UI structure, [static/style.css](static/style.css) for styles.