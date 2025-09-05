import pyodbc
import pandas as pd
import streamlit as st
from dataUtil import util
from dataPlot import plot #Graficas

from src.funciones import mostrar_tablas,filtrar_profesores
from src.agregar_estudiante import agregar_estudiante
from src.agregar_profesor import agregar_profesor

# -------------------------------
# CONEXIÓN A LA BASE DE DATOS
# -------------------------------
server = r'IVANCITO' # Cambia el nombre por el de tu servidor.
database = 'Titulacion_2025'

try:
    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 18 for SQL Server};"
        f"SERVER={server};"
        f"DATABASE={database};"
        "Trusted_Connection=yes;"
        "TrustServerCertificate=yes;"
    )
except Exception as e:
    st.error(f"Error de conexión: {e}")
    st.stop()

# -------------------------------
# INTERFAZ DE USUARIO
# -------------------------------
st.sidebar.title("Opciones de filtrado y búsqueda")

filtrado = st.sidebar.selectbox("Opción de filtrado:", ["Mostrar base de datos", "Filtrar por profesor", "Filtrar por estudiante", "Graficar datos","Agregar estudiante", "Agregar profesor"])

match filtrado:
    case "Mostrar base de datos":
        mostrar_tablas(conn)
    case "Filtrar por profesor":
        filtrar_profesores(conn)
    case "Filtrar por estudiante":
        util.chooseSection(conn)
    case "Graficar datos":
        plot.plotconn(conn)
    case "Agregar estudiante":
        agregar_estudiante(conn)
    case "Agregar profesor":
        agregar_profesor(conn)