# Stargaze 2 — Proyecto Backend con Python, Flask y MySQL

## Descripción

**Stargaze 2** es una aplicación web desarrollada como proyecto backend del curso **Full Stack Python**. Su objetivo es gestionar usuarios y publicaciones sobre observaciones de estrellas mediante una arquitectura organizada en modelos, vistas y controladores (MVC), con persistencia de datos en **MySQL**.

Este repositorio corresponde exclusivamente al proyecto **Stargaze 2**.

## Demostración

- Aplicación publicada: https://examen-stargaze-2.onrender.com/
- Código fuente: https://github.com/KennyLincoln/examen-stargaze-2

> El servicio utiliza alojamiento gratuito, por lo que la primera carga puede tardar algunos segundos mientras se inicia el servidor.

## Funcionalidades

- Registro de usuarios.
- Inicio y cierre de sesión.
- Protección de contraseñas mediante hash con Flask-Bcrypt.
- Creación, visualización, edición y eliminación de publicaciones.
- Validación de formularios.
- Control de autorización para editar o eliminar publicaciones propias.
- Sistema de “Me gusta”.
- Persistencia de usuarios, publicaciones y reacciones en MySQL.

## Tecnologías utilizadas

- Python 3.12
- Flask
- MySQL
- PyMySQL
- Flask-Bcrypt
- Jinja2
- Bootstrap 5
- python-dotenv
- Gunicorn
- Render

## Estructura del proyecto

```text
.
├── server.py
├── requirements.txt
├── Pipfile
├── Pipfile.lock
├── .gitignore
└── flask_app/
    ├── __init__.py
    ├── config/
    │   └── mysqlconnection.py
    ├── controllers/
    │   ├── publicaciones.py
    │   └── usuarios.py
    ├── database/
    │   ├── esquema_publicaciones.mwb
    │   └── esquema_publicaciones.sql
    ├── models/
    │   ├── publicacion.py
    │   └── usuario.py
    └── templates/
        ├── inicio.html
        ├── dashboard.html
        └── editar_publicacion.html
```

## Modelo de datos

La base de datos `esquema_publicaciones` contiene tres tablas relacionadas:

- `usuarios`: almacena los datos de registro y autenticación.
- `publicaciones`: almacena las observaciones creadas por los usuarios.
- `me_gustas`: relaciona usuarios y publicaciones mediante una clave compuesta.

El script para crear la base de datos se encuentra en:

```text
flask_app/database/esquema_publicaciones.sql
```

## Instalación local

### 1. Clonar el repositorio

```bash
git clone https://github.com/KennyLincoln/examen-stargaze-2.git
cd examen-stargaze-2
```

### 2. Crear y activar un entorno virtual

En Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

En Linux o macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instalar las dependencias

```bash
pip install -r requirements.txt
```

### 4. Crear la base de datos

Importar y ejecutar en MySQL el archivo:

```text
flask_app/database/esquema_publicaciones.sql
```

### 5. Configurar las variables de entorno

Crear un archivo `.env` en la raíz del proyecto:

```env
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=tu_contraseña
```

El archivo `.env` está excluido del repositorio mediante `.gitignore` para evitar publicar credenciales.

### 6. Ejecutar la aplicación

```bash
python server.py
```

La aplicación estará disponible localmente en:

```text
http://127.0.0.1:5000/
```

## Autor

**Kenny Lincoln Bugueño Sotelo**  
Ingeniero en Minas y desarrollador en formación.
