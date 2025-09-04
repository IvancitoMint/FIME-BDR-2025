from sqlalchemy import text
import pandas as pd
import streamlit as st

# FORMULARIO PARA AÑADIR PROFESORES (ID automático)

def formulario_agregar_profesor(conn):
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
