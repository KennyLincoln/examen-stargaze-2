# FlorManía Backend — Sistema de Gestión de Publicaciones y Usuarios (Flask)

## 📌 Descripción

Aplicación web desarrollada en **Python con Flask**, orientada a la gestión de **usuarios** y **publicaciones**. El proyecto sigue una arquitectura tipo **MVC (Modelo - Vista - Controlador)**, con conexión a base de datos **MySQL**.

Permite:
- Visualizar un panel principal (dashboard) con las publicaciones existentes.
- Crear, editar y administrar publicaciones.
- Gestionar información de usuarios registrados en el sistema.

> Nota: ajusta esta sección según el alcance real (por ejemplo, si existe login/autenticación, roles de usuario, o CRUD completo).

## 🛠️ Tecnologías utilizadas

- **Python 3**
- **Flask** (framework web)
- **MySQL** (base de datos relacional)
- **Jinja2** (motor de plantillas HTML)
- **MySQL Workbench** (diseño del esquema de base de datos)

## 📂 Estructura del proyecto

```
flask_app/
├── config/
│   └── mysqlconnection.py     # Configuración y conexión a la base de datos
├── controllers/
│   ├── publicaciones.py       # Lógica de negocio para publicaciones
│   └── usuarios.py            # Lógica de negocio para usuarios
├── database/
│   ├── esquema_publicaciones.mwb   # Diagrama del modelo (MySQL Workbench)
│   └── esquema_publicaciones.sql   # Script SQL para crear la base de datos
├── models/
│   ├── publicacion.py         # Modelo de datos: Publicación
│   └── usuario.py             # Modelo de datos: Usuario
├── templates/
│   ├── dashboard.html         # Vista principal con listado de publicaciones
│   ├── editar_publicacion.html# Vista de edición de una publicación
│   └── inicio.html            # Vista de inicio / landing
├── __init__.py
├── requirements.txt
└── .gitignore
```

## ⚙️ Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/KennyLincoln/<nombre-del-repo>.git
cd flask_app
```

### 2. Crear entorno virtual (recomendado)

```bash
python -m venv venv
source venv/bin/activate      # En Windows: venv\Scripts\activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar la base de datos

1. Crear una base de datos en MySQL.
2. Ejecutar el script `database/esquema_publicaciones.sql` para generar las tablas.
3. Configurar las credenciales de conexión en `config/mysqlconnection.py` (usuario, contraseña, host, nombre de la base de datos), idealmente mediante **variables de entorno** en lugar de dejarlas escritas directamente en el código.

Ejemplo con variables de entorno (`.env`):
```
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=tu_password
DB_NAME=flormania_db
```

### 5. Ejecutar la aplicación

```bash
python __init__.py
```

La aplicación quedará disponible en:
```
http://127.0.0.1:5000/
```

## 📸 Capturas de pantalla

> Agrega aquí imágenes del `dashboard.html`, `inicio.html` y `editar_publicacion.html` en funcionamiento, para mostrar visualmente el resultado.

## 🗄️ Modelo de base de datos

El esquema de la base de datos fue diseñado en MySQL Workbench (`esquema_publicaciones.mwb`) e incluye las tablas necesarias para representar la relación entre usuarios y publicaciones. El script SQL correspondiente se encuentra en `database/esquema_publicaciones.sql`.

## 🚧 Próximas mejoras

- Implementar autenticación de usuarios (login / registro).
- Manejo de variables de entorno con `python-dotenv` para proteger credenciales.
- Despliegue en un servicio como Render, Railway o PythonAnywhere.
- Pruebas unitarias para controladores y modelos.

## 👤 Autor

**Kenny Lincoln**
Proyecto desarrollado como parte de práctica/certificación en desarrollo Full Stack Python.
