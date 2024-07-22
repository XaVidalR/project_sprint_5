import pandas as pd
import plotly.express as px
import streamlit as st

vehicles = pd.read_csv(
    'C:/Users/jvida/Desktop/jvidalr/learning/tripleten/project_sprint_5/project_sprint_5/vehicles_us.csv')


st.header('Venta de Vehiculos en Estados Unidos')

st.write('Selecciona el o los tipos de gráficos a crear')
option_1 = st.checkbox('Histograma')
option_2 = st.checkbox('Dispersión')

button = st.button('Construir gráfico(s)')  # crear un botón

if option_1 & option_2:
    if button:
        st.write('Creación de un histograma y gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
        # crear un histograma
        fig = px.histogram(vehicles, x="odometer", title='Histograma')
        # mostrar un gráfico Plotly interactivo
        st.plotly_chart(fig, use_container_width=True)
        # crear un gráfico de dispersión
        disp = px.scatter(vehicles, x="odometer", y="price",title='Gráfico de Dispersión')
        st.plotly_chart(disp, use_container_width=True)
elif option_1:
    if button:
        st.write(
            'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
        # crear un histograma
        hist = px.histogram(vehicles, x="odometer", title='Histograma')
        # mostrar un gráfico Plotly interactivo
        st.plotly_chart(hist, use_container_width=True)
elif option_2:
    if button:
        st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
        # crear un gráfico de dispersión
        disp = px.scatter(vehicles, x="odometer", y="price",title='Gráfico de Dispersión')
        st.plotly_chart(disp, use_container_width=True)
else:
    if button:
      st.write('Debe seleccionar uno o ambos gráficos')
