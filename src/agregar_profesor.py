import pandas as pd
import streamlit as st

def incrementar_ids(conn,prefijo,nombre_base,nombre_id):
    cursor = conn.cursor()

    # Buscar el último Id_profesor
    cursor.execute(f"SELECT MAX({nombre_id}) FROM {nombre_base};")
    ultimo_id = cursor.fetchone()[0]

    # Si no hay profesores, empezamos desde PRF001, de lo contrario se toma la parte numérica y se incrementa en 1
    if ultimo_id is None:
        numero_incrementado = 1
    else:
        ultimo_numero = int(ultimo_id[3:])
        numero_incrementado = ultimo_numero + 1
    return f"{prefijo}{numero_incrementado:03d}"

def agregar_profesor(conn):
    cursor = conn.cursor()
    prefijo = "PRF"
    nombre_base = "Profesor"
    nombre_id = "Id_profesor"
    errores = False

    st.title("Gestión de Profesores")

    nombre_profesor = st.text_input("Nombre del profesor:", max_chars=80)
    if not nombre_profesor.strip():
        st.error("El nombre no puede estar vacío.")
        errores = True
    elif not all(c.isalpha() or c.isspace() for c in nombre_profesor):
        st.error("El nombre solo puede contener letras y espacios.")
        errores = True
    nuevo_id = incrementar_ids(conn,prefijo,nombre_base,nombre_id)

    if st.button("Agregar Profesor") and not errores:
        cursor.execute(
            "INSERT INTO Profesor (Id_profesor, Nombre_profesor) VALUES (?, ?);",
        (nuevo_id, nombre_profesor)
    )
        st.success(f"El profesor {nombre_profesor} fue agregado exitosamente con el ID: {nuevo_id}.")
    conn.commit()
    conn.close()