import pandas as pd
import streamlit as st
import plotly.express as px

# Leer el archivo CSV
df_vehiculos = pd.read_csv(r'C:\Users\achav\Documents\proyectos\WEBAUTOS\vehicles_us.csv')


st.header ('Análisis de vehículos usados')

#Crear un botón para construir el histograma
hist_button = st.button('Construir histograma') # crear un botón

if hist_button: # al hacer clic en el botón
    st.subheader("Histograma de precios de vehículos")
       
     # crear un histograma
    fig = px.histogram(df_vehiculos, x="price", title="Distribución de Precios de Vehículos", nbins=30)
     
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


#Construir botón para crear un gráfico de dispersión
disp_button = st.button('Construir diagrama de dispersión') # crear un botón

if disp_button: # al hacer clic en el botón
    st.subheader ("Diagrama de Dispersión: Kilometraje vs Precio")
    st.write ('Diagrama de dispersión')

    fig = px.scatter(df_vehiculos, x="odometer", y="price", 
                 title="Relación entre Kilometraje y Precio de Vehículos",
                 labels={"odometer": "Kilometraje (millas)", "price": "Precio ($)"},
                 opacity=0.6)

    st.plotly_chart(fig, use_container_width=True)