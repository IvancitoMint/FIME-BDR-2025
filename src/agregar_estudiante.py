import pandas as pd
import streamlit as st

def incrementar_ids(conn,prefijo,nombre_base,nombre_id):
    cursor = conn.cursor()

    # Buscar el último Id_profesor
    cursor.execute(f"SELECT MAX({nombre_id}) FROM {nombre_base};")
    ultimo_id = cursor.fetchone()[0]

    # Si no hay registros, empezamos desde 001, de lo contrario se toma la parte numérica y se incrementa en 1
    if ultimo_id is None:
        numero_incrementado = 1
    else:
        ultimo_numero = int(ultimo_id[3:])
        numero_incrementado = ultimo_numero + 1
    return f"{prefijo}{numero_incrementado:03d}"

def agregar_estudiante(conn):
    cursor = conn.cursor()
    prefijo1 = "202"
    nombre_base1 = "Titulacion"
    nombre_id1 = "Id_titulacion"
    Id_titulacion = incrementar_ids(conn,prefijo1,nombre_base1,nombre_id1)
    prefijo2 = "202"
    nombre_base2 = "Estudiante"
    nombre_id2 = "Id_estudiante"
    Id_estudiante = incrementar_ids(conn,prefijo2,nombre_base2,nombre_id2)
    errores = False
    # Consultas para selectbox y diccionario de carreras
    cursor.execute("SELECT Id_carrera, Nombre_carrera FROM Carrera;")
    carreras = cursor.fetchall()
    carreras_dicc = {nombre: idc for idc, nombre in carreras}
    # Consultas para selectbox y diccionario de modalidades
    cursor.execute("SELECT Id_modalidad, nombre_modalidad FROM Modalidad;")
    modalidades = cursor.fetchall()
    modalidades_dicc = {nombre: idm for idm, nombre in modalidades}
    # Consultas para selectbox y diccionario de profesores
    cursor.execute("SELECT Id_profesor, Nombre_profesor FROM Profesor;")
    profesores = cursor.fetchall()
    profesores_dicc = {nombre: idp for idp, nombre in profesores}

    st.title("Gestión de Estudiantes")

    # Nombre del estudiante
    Nombre_estudiante = st.text_input("Nombre del estudiante:", max_chars=80)
    if not Nombre_estudiante.strip():
        st.error("El nombre no puede estar vacío.")
        errores = True
    elif not all(c.isalpha() or c.isspace() for c in Nombre_estudiante):
        st.error("El nombre solo puede contener letras y espacios.")
        errores = True

    # Generación del estudiante
    generacion = st.text_input("Generación del estudiante (formato ejemplo: 2020-2025):", max_chars=9)
    if not generacion:
        st.error("La generación no puede estar vacía.")
        errores = True
    elif not all(c.isdigit() or c == '-' for c in generacion):
        st.error("La generación solo puede contener números y un guión.")
        errores = True

    # Carrera del estudiante
    opcion_carrera = st.selectbox("Selecciona una carrera:", list(carreras_dicc.keys()))
    if opcion_carrera:
        id_carrera = carreras_dicc[opcion_carrera]

    # Modalidad del estudiante
    opcion_modalidad = st.selectbox("Selecciona una modalidad:", list(modalidades_dicc.keys()))
    if opcion_modalidad:
        Id_modalidad = modalidades_dicc[opcion_modalidad]

    if Id_modalidad == "MD1" or Id_modalidad == "MD2" or Id_modalidad == "MD3" or Id_modalidad == "MD4" or Id_modalidad == "MD5":
        Nombre_proyecto = st.text_input("Nombre del proyecto:", max_chars=100)
        if not Nombre_proyecto.strip():
            st.error("El nombre del proyecto no puede estar vacío.")
            errores = True
        elif not all(c.isalpha() or c.isspace() for c in Nombre_proyecto):
            st.error("El nombre solo puede contener letras y espacios.")
            errores = True
    elif Id_modalidad == "MD6" or Id_modalidad == "MD7" or Id_modalidad == "MD8" or Id_modalidad == "MD9":
        Nombre_proyecto = "N/A"

    # Fecha de titulación
    Fecha_titulacion = st.date_input("Fecha de titulación (Formato: YYYY-MM-DD):")

    # Roles de profesores
    if Id_modalidad == "MD1" or Id_modalidad == "MD2" or Id_modalidad == "MD3" or Id_modalidad == "MD4" or Id_modalidad == "MD5":
        st.subheader("Asignación de roles a profesores")
        opcion_asesor = st.selectbox("Selecciona al Asesor:", list(profesores_dicc.keys()), key="Asesor")
        if opcion_asesor:
            id_asesor = profesores_dicc[opcion_asesor]
        if opcion_coasesor := st.selectbox("Selecciona al Coasesor:", list(profesores_dicc.keys()), key="Coasesor"):
            id_coasesor = profesores_dicc[opcion_coasesor]
        if opcion_presidente := st.selectbox("Selecciona al Presidente:", list(profesores_dicc.keys()), key="Presidente"):
            id_presidente = profesores_dicc[opcion_presidente]
        if opcion_secretario := st.selectbox("Selecciona al Secretario:", list(profesores_dicc.keys()), key="Secretario"):
            id_secretario = profesores_dicc[opcion_secretario]
        if opcion_vocal := st.selectbox("Selecciona al Vocal:", list(profesores_dicc.keys()), key="Vocal"):
            id_vocal = profesores_dicc[opcion_vocal]
        # Validaciones de roles
        if opcion_asesor == opcion_coasesor or opcion_asesor == opcion_presidente or opcion_asesor == opcion_secretario:
            st.error("El Asesor no puede ser el mismo que el Coasesor, Presidente o Secretario.")
            errores = True
        if opcion_coasesor == opcion_presidente or opcion_coasesor == opcion_secretario or opcion_coasesor == opcion_vocal:
            st.error("El Coasesor no puede ser el mismo que el Presidente, Secretario o Vocal.")
            errores = True
        if opcion_presidente == opcion_secretario or opcion_presidente == opcion_vocal:
            st.error("El Presidente no puede ser el mismo que el Secretario o Vocal.")
            errores = True
    elif Id_modalidad == "MD6" or Id_modalidad == "MD7" or Id_modalidad == "MD8" or Id_modalidad == "MD9":
        if opcion_presidente := st.selectbox("Selecciona al Presidente:", list(profesores_dicc.keys()), key="Presidente"):
            id_presidente = profesores_dicc[opcion_presidente]
        if opcion_secretario := st.selectbox("Selecciona al Secretario:", list(profesores_dicc.keys()), key="Secretario"):
            id_secretario = profesores_dicc[opcion_secretario]
        if opcion_vocal := st.selectbox("Selecciona al Vocal:", list(profesores_dicc.keys()), key="Vocal"):
            id_vocal = profesores_dicc[opcion_vocal]
        # Validaciones de roles
        if opcion_presidente == opcion_secretario or opcion_presidente == opcion_vocal:
            st.error("El Presidente no puede ser el mismo que el Secretario o Vocal.")
            errores = True
        if opcion_secretario == opcion_vocal:
            st.error("El Secretario no puede ser el mismo que el Vocal.")
            errores = True

    if st.button("Agregar Estudiante") and not errores:
        cursor.execute(
            "INSERT INTO Estudiante (Id_estudiante, Nombre_estudiante, Generacion, Id_carrera) VALUES (?, ?, ?, ?);",
            (Id_estudiante, Nombre_estudiante, generacion, id_carrera)
        )
        cursor.execute(
            "INSERT INTO Titulacion (Id_titulacion, Id_estudiante, Id_modalidad, Nombre_proyecto, Fecha_titulacion) VALUES (?, ?, ?, ?, ?);",
            (Id_titulacion, Id_estudiante, Id_modalidad, Nombre_proyecto, Fecha_titulacion)
        )
        # Asignación de profesores según modalidad
        if Id_modalidad == "MD1" or Id_modalidad == "MD2" or Id_modalidad == "MD3" or Id_modalidad == "MD4" or Id_modalidad == "MD5":
            cursor.execute(
                "INSERT INTO Titulacion_profesor (Id_titulacion, Id_profesor, Rol) VALUES (?, ?, ?);",
                (Id_titulacion, id_asesor, "Asesor")
            )
            cursor.execute(
                "INSERT INTO Titulacion_profesor (Id_titulacion, Id_profesor, Rol) VALUES (?, ?, ?);",
                (Id_titulacion, id_coasesor, "Coasesor")
            )
            cursor.execute(
                "INSERT INTO Titulacion_profesor (Id_titulacion, Id_profesor, Rol) VALUES (?, ?, ?);",
                (Id_titulacion, id_presidente, "Presidente")
            )
            cursor.execute(
                "INSERT INTO Titulacion_profesor (Id_titulacion, Id_profesor, Rol) VALUES (?, ?, ?);",
                (Id_titulacion, id_secretario, "Secretario")
            )
            cursor.execute(
                "INSERT INTO Titulacion_profesor (Id_titulacion, Id_profesor, Rol) VALUES (?, ?, ?);",
                (Id_titulacion, id_vocal, "Vocal")
            )
        elif Id_modalidad == "MD6" or Id_modalidad == "MD7" or Id_modalidad == "MD8" or Id_modalidad == "MD9":
            cursor.execute(
                "INSERT INTO Titulacion_profesor (Id_titulacion, Id_profesor, Rol) VALUES (?, ?, ?);",
                (Id_titulacion, id_presidente, "Presidente")
            )
            cursor.execute(
                "INSERT INTO Titulacion_profesor (Id_titulacion, Id_profesor, Rol) VALUES (?, ?, ?);",
                (Id_titulacion, id_secretario, "Secretario")
            )
            cursor.execute(
                "INSERT INTO Titulacion_profesor (Id_titulacion, Id_profesor, Rol) VALUES (?, ?, ?);",
                (Id_titulacion, id_vocal, "Vocal")
            )
        st.success(f"El estudiante {Nombre_estudiante} fue agregado exitosamente con el ID de titulacion: {Id_titulacion} y el ID de estudiante: {Id_estudiante}.")
    conn.commit()
    conn.close()