import streamlit as st
import pandas as pd
from numpy import append
import plotly.express as px #Es necesario descargarla en venv

def plotconn(conn):
    opt = st.selectbox("Seleccione las categorias a graficar:", 
                         ["Modalidades", "Carreras", "Profesor/Roles"],
                         None)
    if opt:
        createPlot(opt, conn)

def createPlot(opt,conn):
    global textTitle
    textTitle = ""
    dirValuesNames = {'values':[],'names':[]}
    if opt == "Modalidades":
        dfNames=pd.read_sql("SELECT Nombre_modalidad FROM Modalidad",conn)
        dfData=pd.read_sql("SELECT Id_modalidad FROM Titulacion",conn)
        dirValuesNames["names"] = [row[0] for row in dfNames.values.tolist()]
        data = [row[0] for row in dfData.values.tolist()]
        contValues = {
            'MD1':0,
            'MD2':0,
            'MD3':0,
            'MD4':0,
            'MD5':0,
            'MD6':0,
            'MD7':0,
            'MD8':0,
            'MD9':0
        }
        n = len(data)
        for d in data:
            if d in contValues:
                contValues[d]+=1 #podria contar las coincidencias con .count pero preferi hacerlo manual
        for c in contValues:
            dirValuesNames['values'].append(int((int(contValues[c])*n)/100))
        textTitle = "Dritribución de Modalidades de Titulación"

    if opt == "Carreras":
        fac= st.selectbox("Graficar por:", 
                            ["Global","Facultad"],
                            None)
        if fac=="Global":
            dfData=pd.read_sql("SELECT Estudiante.Id_carrera "+
                                "FROM (((Titulacion "+
                                "INNER JOIN Estudiante ON Titulacion.Id_estudiante = Estudiante.Id_estudiante)"+
                                "INNER JOIN Carrera ON Estudiante.Id_carrera = Carrera.Id_carrera)"+
                                "INNER JOIN Facultad ON Carrera.Id_facultad = Facultad.Id_facultad)",conn)
            data = [row[0] for row in dfData.values.tolist()]
            contValues = {
                'CRR001':int(data.count('CRR001')),
                'CRR002':int(data.count('CRR002')),
                'CRR003':int(data.count('CRR003')),
                'CRR004':int(data.count('CRR004')),
                'CRR005':int(data.count('CRR005')),
                'CRR006':int(data.count('CRR006')),
                'CRR007':int(data.count('CRR007')),
                'CRR008':int(data.count('CRR008')),
                'CRR009':int(data.count('CRR009')),
                'CRR0010':int(data.count('CRR0010')),
                'CRR0011':int(data.count('CRR0011')),
                'CRR0012':int(data.count('CRR0012')),
                'CRR0013':int(data.count('CRR0013')),
                'CRR0014':int(data.count('CRR0014')),
                'CRR0015':int(data.count('CRR0015')),
                'CRR0016':int(data.count('CRR0016')),
                'CRR0017':int(data.count('CRR0017')),
                'CRR0018':int(data.count('CRR0018')),
                'CRR0019':int(data.count('CRR0019')),
                'CRR0020':int(data.count('CRR0020'))
            }
            n = len(data)
            for c in contValues:
                dirValuesNames['values'].append(int((int(contValues[c])*n)/100))
            dfNames=pd.read_sql("SELECT Nombre_carrera FROM Carrera",conn)
            dirValuesNames["names"] = [row[0] for row in dfNames.values.tolist()]
        
        elif fac=="Facultad":
            facu = st.selectbox("Facultad", pd.read_sql("SELECT Nombre_facultad FROM Facultad", conn))
            dfData = pd.read_sql(f"""
                SELECT Estudiante.Id_carrera
                FROM Titulacion
                INNER JOIN Estudiante ON Titulacion.Id_estudiante = Estudiante.Id_estudiante
                INNER JOIN Carrera ON Estudiante.Id_carrera = Carrera.Id_carrera
                INNER JOIN Facultad ON Carrera.Id_facultad = Facultad.Id_facultad
                WHERE Facultad.Nombre_facultad = '{facu}'
            """, conn)
            data = [row[0] for row in dfData.values.tolist()]
            contValues = {
                'CRR001':int(data.count('CRR001')),
                'CRR002':int(data.count('CRR002')),
                'CRR003':int(data.count('CRR003')),
                'CRR004':int(data.count('CRR004')),
                'CRR005':int(data.count('CRR005')),
                'CRR006':int(data.count('CRR006')),
                'CRR007':int(data.count('CRR007')),
                'CRR008':int(data.count('CRR008')),
                'CRR009':int(data.count('CRR009')),
                'CRR0010':int(data.count('CRR0010')),
                'CRR0011':int(data.count('CRR0011')),
                'CRR0012':int(data.count('CRR0012')),
                'CRR0013':int(data.count('CRR0013')),
                'CRR0014':int(data.count('CRR0014')),
                'CRR0015':int(data.count('CRR0015')),
                'CRR0016':int(data.count('CRR0016')),
                'CRR0017':int(data.count('CRR0017')),
                'CRR0018':int(data.count('CRR0018')),
                'CRR0019':int(data.count('CRR0019')),
                'CRR0020':int(data.count('CRR0020'))
            }
            n = len(data)
            for c in contValues:
                dirValuesNames['values'].append(int((int(contValues[c])*n)/100))
            dfNames=pd.read_sql("SELECT Nombre_carrera FROM Carrera",conn)
            dirValuesNames["names"] = [row[0] for row in dfNames.values.tolist()]
        textTitle = "Dritribución de Carreras"

    if opt == "Profesor/Roles":
        opGrafProf= st.selectbox("Graficar por:", 
                            ["Roles","Profesor"],
                            None)
        if opGrafProf == "Roles":
            dfData = pd.read_sql(f"""
                SELECT Titulacion_Profesor.Rol 
                FROM Titulacion
                INNER JOIN Titulacion_Profesor ON Titulacion.Id_titulacion = Titulacion_Profesor.Id_titulacion
                INNER JOIN Profesor ON Profesor.Id_profesor = Titulacion_Profesor.Id_profesor
            """, conn)
            data = [row[0] for row in dfData.values.tolist()]
            contValues = {
                'Asesor':int(data.count('Asesor')),
                'Co-asesor':int(data.count('Co-asesor')),
                'Presidente':int(data.count('Presidente')),
                'Secretario':int(data.count('Secretario')),
                'Vocal':int(data.count('Vocal'))
            }
            n = len(data)
            for c in contValues:
                dirValuesNames['values'].append(int((int(contValues[c])*n)/100))
            dirValuesNames["names"] = ["Asesor","Co-asesor","Presidente","Secretario","Vocal"]
            textTitle = "Dritribución de los Roles"

        if opGrafProf == "Profesor":
            prof = st.selectbox("Profesor: ", pd.read_sql("SELECT Nombre_profesor FROM Profesor", conn))
            dfData = pd.read_sql(f"""
                SELECT Titulacion_Profesor.Rol
                FROM Titulacion
                INNER JOIN Titulacion_Profesor ON Titulacion.Id_titulacion = Titulacion_Profesor.Id_titulacion
                INNER JOIN Profesor ON Profesor.Id_profesor = Titulacion_Profesor.Id_profesor
                WHERE Profesor.Nombre_profesor = '{prof}'
            """, conn)
            data = [row[0] for row in dfData.values.tolist()]
            contValues = {
                'Asesor':int(data.count('Asesor')),
                'Co-asesor':int(data.count('Co-asesor')),
                'Presidente':int(data.count('Presidente')),
                'Secretario':int(data.count('Secretario')),
                'Vocal':int(data.count('Vocal'))
            }
            n = len(data)
            for c in contValues:
                dirValuesNames['values'].append(int((int(contValues[c])*n)/100))
            dirValuesNames["names"] = ["Asesor","Co-asesor","Presidente","Secretario","Vocal"]
            textTitle = "Dritribución de Roles del Profesor"
    df = pd.DataFrame(dirValuesNames)
    fig = px.pie(df, values='values', names='names', title=textTitle)
    st.plotly_chart(fig, use_container_width=True)


