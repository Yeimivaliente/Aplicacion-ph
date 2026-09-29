import streamlit as st

st.title("Evaluación de un lote")

pH = st.number_input(
    "pH",
    value=6.5
)

temperatura = st.number_input(
    "Temperatura (°C)",
    value=23.0
)

if st.button("Evaluar"):
    # Lógica de evaluación según las reglas
    if pH < 6.0 or pH > 7.0:
        resultado = "Revisar pH"
    elif temperatura < 20.0 or temperatura > 25.0:
        resultado = "Revisar temperatura"
    else:
        resultado = "Lote aceptable"

    # Mostrar resultado
    st.write(f"Resultado: {resultado}")
import streamlit as st

# Barra lateral (Sidebar)
st.sidebar.title("Información extra")
st.sidebar.write("**Descripción:** Aplicación para evaluar la calidad de un lote según pH y temperatura.")
st.sidebar.write("**Nombre:** Yeimi Valiente Cervantes")
st.sidebar.write("**Grupo:** 3L")
st.sidebar.write("**Facultad:** Facultad de Ciencias Químicas")

# Contenido principal
st.title("Evaluación de un lote")

pH = st.number_input(
    "pH",
    value=6.5
)

temperatura = st.number_input(
    "Temperatura (°C)",
    value=23.0
)

if st.button("Evaluar"):
    # Lógica de evaluación según las reglas
    if pH < 6.0 or pH > 7.0:
        resultado = "Revisar pH"
    elif temperatura < 20.0 or temperatura > 25.0:
        resultado = "Revisar temperatura"
    else:
        resultado = "Lote aceptable"

    # Mostrar resultado
    st.write(f"Resultado: {resultado}")
