import pandas as pd
import streamlit as st

def mostrar_tablas(conn):
        df_estudiantes = pd.read_sql("SELECT * FROM Estudiante", conn)
        df_profesores = pd.read_sql("SELECT * FROM Profesor", conn)
        df_carreras = pd.read_sql("SELECT * FROM Carrera", conn)
        df_modalidades = pd.read_sql("SELECT * FROM Modalidad", conn)

        st.title("Base de Datos de Titulación")

        st.subheader("Estudiantes")
        st.dataframe(df_estudiantes)

        st.subheader("Profesores")
        st.dataframe(df_profesores)

        st.subheader("Carreras")
        st.dataframe(df_carreras)

        st.subheader("Modalidades")
        st.dataframe(df_modalidades)

def filtrar_profesores(conn):
    st.title("Filtrar Alumnos por Profesor")        
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
        st.subheader(f"Alumnos asignados a {nombre_profesor}")
        st.dataframe(df_resultado)

    # Grafica