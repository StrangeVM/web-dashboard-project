import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar el archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado de la aplicación
st.header("Dashboard de Análisis de Vehículos")

# Botón para mostrar el histograma
if st.button('Mostrar histograma'):
    st.write('Histograma del odómetro:')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Botón para mostrar el gráfico de dispersión
if st.button('Mostrar gráfico de dispersión'):
    st.write('Gráfico de dispersión (odómetro vs precio):')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)