from asyncio.windows_events import NULL
from typing import final
from numpy import append
import pyodbc
import pandas as pd
import streamlit as st

def chooseSection(conn):
    opt = st.multiselect("Seleccione las categorias a filtrar", 
                         ["No. de Cuenta", "Modalidad", "Carrera", "Fecha de titulacion", "Profesor"])
    if opt:
        createSection(opt, conn)

def formatList(data:list):
    result = ""
    for i in range(len(data)):
        if i < len(data)-1:
            result = f"{result}{data[i]},"
        else:
            result += f"{data[i]}"

    return result

def createSection(opts:list, conn):
    global nc, mod, car, date, prf, finalText, stQuery
    nc = 0
    mod, car, date, prf = ("", "", "", "")
    finalText = ""
    stQuery = []
    stQuery.append("Estudiante.Id_estudiante")
    stQuery.append("Estudiante.Nombre_estudiante")
    stQuery.append("Facultad.Nombre_facultad")
    stQuery.append("Carrera.Nombre_carrera")
    for opt in opts:
        if opt == "No. de Cuenta":
            nc = st.number_input("No. de cuenta", min_value=200000, step=1)
            finalText = f"{finalText}, su No. de Cuenta"
        if opt == "Carrera":
            car = st.multiselect("Carrera", pd.read_sql("SELECT Nombre_carrera FROM Carrera", conn))
            finalText = f"{finalText}, su {opt} actual"
        if opt == "Modalidad":
            mod = st.multiselect("Modalidad", pd.read_sql("SELECT Nombre_modalidad FROM Modalidad ", conn))
            stQuery.append("Modalidad.Nombre_modalidad")
            finalText = f"{finalText}, su {opt} de titulacion"
        if opt == "Fecha de titulacion":
            date = st.multiselect("fecha", pd.read_sql("SELECT DISTINCT Fecha_titulacion FROM Titulacion ", conn))
            stQuery.append("Titulacion.Fecha_titulacion")
            finalText = f"{finalText}, su {opt}"
        if opt == "Profesor":
            prf = st.multiselect("Profesor", pd.read_sql("SELECT Nombre_profesor FROM Profesor ", conn))
            stQuery.append("Profesor.Nombre_profesor")
            stQuery.append("Titulacion_Profesor.Rol")
            finalText = f"{finalText}, su {opt} encargado"


    doFilter = st.button("Filtrar")
    if doFilter:
        daQuery = formatList(stQuery)
        finalQuery = (f"SELECT {daQuery} FROM Estudiante, Carrera, Facultad, Profesor, Modalidad, Titulacion, Titulacion_Profesor" + 
                           " WHERE Estudiante.Id_estudiante = Titulacion.Id_estudiante"+
                           " AND Carrera.Id_carrera = Estudiante.Id_carrera"+
                           " AND Carrera.Id_facultad = Facultad.Id_facultad"+
                           " AND Modalidad.Id_modalidad = Titulacion.Id_modalidad"+
                           " AND Titulacion_Profesor.Id_titulacion = Titulacion.Id_titulacion"+
                           " AND Titulacion_Profesor.Id_profesor = Profesor.Id_profesor")
        if nc:
            finalQuery += f" AND Estudiante.Id_estudiante = {nc}"
        if car:
            finalQuery += f" AND Carrera.Nombre_carrera = '{car[0]}'"
        if mod:
            finalQuery += f" AND Modalidad.Id_modalidad = '{mod[0]}'"
        if date:
            finalQuery += f" AND Titulacion.Fecha_titulacion = '{date[0]}'"
        if prf:
            finalQuery += f" AND Profesor.Nombre_profesor = '{prf[0]}'"
            #Agregar iteracion para la lista de valores obtenidos en cada consulta, o directamente
            #cambiar el tipo de input por uno que no deje elejir mas de 1
        #st.text(finalQuery)
        data = pd.read_sql(finalQuery, conn)
        st.subheader(f"Datos filtrados en relacion a{finalText}")
        st.dataframe(data)
    

    