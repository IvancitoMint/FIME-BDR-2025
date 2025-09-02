# Manual de instalación y ejecución de la app Streamlit con SQL Server

## 1. Requisitos previos

Antes de iniciar, asegúrate de tener:

- Python 3.13 instalado en tu sistema.
- SQL Server instalado y corriendo en tu máquina.
- Tablas de la base de datos `Titulacion_2025` creadas y con datos.

---

## 2. Creación del entorno virtual

Usaremos un **entorno virtual** para evitar conflictos de librerías entre proyectos.

1. Abre la consola (CMD) dentro de la carpeta del proyecto en VSC:
2. Ejecuta en orden los siguientes comandos:
3. -m venv venv
4. venv\Scripts\activate
5. Si realziaron la creación y activacón bien, a la derecha de la ruta les debe aparecen **(venv)**
5. pip install streamlit pandas pyodbc

## 3. Drivers ODBC para SQL Server
La librería pyodbc necesita un driver ODBC para conectarse a SQL Server.
Para esta app se utiliza: ODBC Driver 18 for SQL Server
Descargar e instalar el archivo adjunto llamado: msodbcsql.msi

## 4. Conexión a la BD
Ejecutar los archivos .sql en orden que se encuentran en la carpeta **SQL**
Una vez creada la BD, las tablas y haberlas llenado, sigue hacer la conexión.
- Con **Windows Authentication**
server = r'TUSERVER' 
En el código, en la línea 8, solamente necesitan cambiar el "TU_SERVER" por el nombre de su servidor.
Lo encuentran al abrir Microsoft SQL SERVER como **Server Name:**

- Con **Usuario y contraseña**
En este caso, en el código, debrán de agregar un par de cosas:
server = r'TU_SERVER'       # Cambia por tu servidor
database = 'Titulacion_2025'
username = 'TU_USER'        # Tu usuario de SQL SERVER
password = 'TU_PASSWORD'    # Tu contraseña de SQL SERVER

conn = pyodbc.connect(
    f"DRIVER={{ODBC Driver 18 for SQL Server}};"
    f"SERVER={server};"
    f"DATABASE={database};"
    f"UID={username};"
    f"PWD={password};"
    "TrustServerCertificate=yes;"
)

## 5. Ejecutar la app Streamlit
Siempre que vayan a ejecutar la app de Streamlit tendrán que hacerlo dentro del entorno virtual.
Ejecutando los siguientes comandos desde la terminal.
1. venv\Scripts\activate
2. streamlit run index.py