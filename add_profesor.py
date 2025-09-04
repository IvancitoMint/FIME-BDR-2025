import pandas as pd
import streamlit as st
from sqlalchemy import create_engine, text

# -------------------------------
# CONEXIÓN A LA BASE DE DATOS
# -------------------------------
server = r'PCDEMAURICIO'   
database = 'Titulacion_2025'
username = 'sa'
password = '*********'

# Cadena de conexión con SQLAlchemy
conn_str = (
    f"mssql+pyodbc://{username}:{password}@{server}/{database}"
    "?driver=ODBC+Driver+17+for+SQL+Server"
    "&TrustServerCertificate=yes"
)

try:
    engine = create_engine(conn_str)
    conn = engine.connect()
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
st.title("📚 Base de Datos de Titulación")

st.subheader("👨‍🎓 Estudiantes")
st.dataframe(df_estudiantes)

st.subheader("🎓 Titulaciones")
st.dataframe(df_titulaciones)

st.subheader("👩‍🏫 Profesores")
st.dataframe(df_profesores)

# -------------------------------
# FILTRO INTERACTIVO
# -------------------------------
nombre_profesor = st.text_input("Buscar alumnos por profesor:")
if nombre_profesor:
    query = text("""
        SELECT p.Nombre_profesor, e.Id_estudiante, e.Nombre_estudiante, tp.Rol
        FROM Profesor p
        JOIN Titulacion_Profesor tp ON p.Id_profesor = tp.Id_profesor
        JOIN Titulacion t ON tp.Id_titulacion = t.Id_titulacion
        JOIN Estudiante e ON t.Id_estudiante = e.Id_estudiante
        WHERE p.Nombre_profesor LIKE :nombre
    """)
    df_resultado = pd.read_sql(query, conn, params={"nombre": f"%{nombre_profesor}%"})
    st.subheader(f"🔎 Alumnos asignados a {nombre_profesor}")
    st.dataframe(df_resultado)

# -------------------------------
# FORMULARIO PARA AÑADIR PROFESORES (ID automático)
# -------------------------------
st.subheader("Añadir nuevo profesor")

# Calcular automáticamente el siguiente ID
query_last_id = "SELECT TOP 1 Id_profesor FROM Profesor ORDER BY Id_profesor DESC"
ultimo = pd.read_sql(query_last_id, conn)

if not ultimo.empty:
    ultimo_id = ultimo.iloc[0, 0]  # ejemplo: 'PRF015'
    ultimo_num = int(ultimo_id.replace("PRF", ""))
    nuevo_id = f"PRF{ultimo_num+1:03d}"  # genera PRF016, PRF017...
else:
    nuevo_id = "PRF001"  # si no hay profesores aún

st.write(f"El ID generado automáticamente será: **{nuevo_id}**")

# Inputs solo para nombre y confirmación
nuevo_nombre = st.text_input("Nombre del profesor")
confirmar = st.checkbox("Confirmo que los datos son correctos")

if st.button("Guardar profesor"):
    if not nuevo_nombre:
        st.warning("Por favor, ingresa el nombre del profesor antes de guardar.")
    elif not confirmar:
        st.warning("Debes confirmar los datos antes de guardar.")
    else:
        try:
            insert_query = text("""
                INSERT INTO Profesor (Id_profesor, Nombre_profesor)
                VALUES (:id, :nombre)
            """)
            conn.execute(insert_query, {"id": nuevo_id, "nombre": nuevo_nombre})
            conn.commit()
            st.success(f"Profesor '{nuevo_nombre}' añadido correctamente con ID {nuevo_id}.")

            # Recargar lista de profesores
            df_profesores = pd.read_sql("SELECT * FROM Profesor", conn)
            st.dataframe(df_profesores)

        except Exception as e:
            st.error(f"Error al insertar profesor: {e}")
