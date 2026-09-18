**# stargaze Backend — Sistema de Publicaciones y Usuarios (Flask)**

**## 📌 Descripción**

Aplicación web desarrollada en **\*\*Python con Flask\*\***, orientada a la gestión de **\*\*usuarios\*\*** y **\*\*publicaciones\*\***. El proyecto utiliza una arquitectura tipo **\*\*MVC (Modelo - Vista - Controlador)\*\***, con conexión a base de datos **\*\*MySQL\*\***.

Permite:

\- Registrar usuarios e iniciar sesión

\- Visualizar en un panel principal las publicaciones existentes.

\- Crear, editar y administrar publicaciones.

\- Dar "Me Gusta" a una publicación.


**## 🛠️ Tecnologías utilizadas**

\- **\*\*Python 3\*\***

\- **\*\*Flask\*\*** (framework web)

\- **\*\*MySQL\*\*** (base de datos relacional)

\- **\*\*Jinja2\*\*** (motor de plantillas HTML)

\- **\*\*MySQL Workbench\*\*** (diseño del esquema de base de datos)

**## 📂 Estructura del proyecto**

\`\`\`

flask\_app/

├── config/

│   └── mysqlconnection.py     # Configuración y conexión a la base de datos

├── controllers/

│   ├── publicaciones.py       # Lógica de negocio para publicaciones

│   └── usuarios.py            # Lógica de negocio para usuarios

├── database/

│   ├── esquema\_publicaciones.mwb   # Diagrama del modelo (MySQL Workbench)

│   └── esquema\_publicaciones.sql   # Script SQL para crear la base de datos

├── models/

│   ├── publicacion.py         # Modelo de datos: Publicación

│   └── usuario.py             # Modelo de datos: Usuario

├── templates/

│   ├── dashboard.html         # Vista principal con listado de publicaciones

│   ├── editar\_publicacion.html# Vista de edición de una publicación

│   └── inicio.html            # Vista de inicio / landing

├── \_\_init\_\_.py

├── requirements.txt

└── .gitignore

\`\`\`

**## ⚙️ Instalación y ejecución**

**### 1. Clonar el repositorio**

\`\`\`bash

git clone [https://github.com/KennyLincoln/](https://github.com/KennyLincoln/)\<nombre-del-repo>.git

cd flask\_app

\`\`\`

**### 2. Crear entorno virtual (recomendado)**

\`\`\`bash

pip install pipenv

\`\`\`

**### 3. Instalar dependencias**

\`\`\`bash

pip install -r requirements.txt

\`\`\`

**### 4. Configurar la base de datos**

1\. Crear una base de datos en MySQL.

2\. Ejecutar el script \`database/esquema\_publicaciones.sql\` para generar las tablas.

3\. Configurar las credenciales de conexión en \`config/mysqlconnection.py\` (usuario, contraseña, host, nombre de la base de datos), idealmente mediante **\*\*variables de entorno\*\*** en lugar de dejarlas escritas directamente en el código.

Ejemplo con variables de entorno (\`.env\`):

\`\`\`

DB\_HOST=localhost

DB\_PORT=3306

DB\_USER=root

DB\_PASSWORD=tu\_password

DB\_NAME=tu\_nombre

\`\`\`

**### 5. Ejecutar la aplicación**

\`\`\`bash

pipenv shell

python server.py

\`\`\`

La aplicación publicada quedará disponible en:

\`\`\`

[https://examen-stargaze-2.onrender.com/](https://examen-stargaze-2.onrender.com/)

\`\`\`

**## 👤 Autor**

**\*\*Kenny Lincoln Bugueño Sotelo\*\***
