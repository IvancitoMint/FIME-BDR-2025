import pyodbc
import pandas as pd
import streamlit as st
from dataUtil import util

# -------------------------------
# CONEXIÓN A LA BASE DE DATOS
# -------------------------------
server = r'DESKTOP-ONNPS1D' # Cambia el nombre por el de tu servidor.
server = r'DESKTOP-GU8C6K2' # Cambia el nombre por el de tu servidor.
database = 'Titulacion_2025'

try:
    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 18 for SQL Server};"
        f"SERVER={server};"
        f"DATABASE={database};"
        "Trusted_Connection=yes;"
        "TrustServerCertificate=yes;"
    )
    st.success("Conexión exitosa a la base de datos")
except Exception as e:
    st.error(f"Error de conexión: {e}")
    st.stop()

# -------------------------------
# CARGA DE TABLAS
# -------------------------------
df_estudiantes = pd.read_sql("SELECT * FROM Estudiante", conn)
df_titulaciones = pd.read_sql("SELECT * FROM Titulacion", conn)
df_profesores = pd.read_sql("SELECT * FROM Profesor", conn)

# -------------------------------
# APP STREAMLIT
# -------------------------------
st.title("Base de Datos de Titulación")

st.subheader("Estudiantes")
st.dataframe(df_estudiantes)

st.subheader("Titulaciones")
st.dataframe(df_titulaciones)

st.subheader("Profesores")
st.dataframe(df_profesores)

# -------------------------------
# FILTRO INTERACTIVO
# -------------------------------
nombre_profesor = st.text_input("Buscar alumnos por profesor:")
if nombre_profesor:
    query = f"""
    SELECT p.Nombre_profesor, e.Id_estudiante, e.Nombre_estudiante, tp.Rol
    FROM Profesor p
    JOIN Titulacion_Profesor tp ON p.Id_profesor = tp.Id_profesor
    JOIN Titulacion t ON tp.Id_titulacion = t.Id_titulacion
    JOIN Estudiante e ON t.Id_estudiante = e.Id_estudiante
    WHERE p.Nombre_profesor LIKE ?
    """
    df_resultado = pd.read_sql(query, conn, params=[f"%{nombre_profesor}%"])
    st.subheader(f"🔎 Alumnos asignados a {nombre_profesor}")
    st.dataframe(df_resultado)

util.chooseSection(conn)
