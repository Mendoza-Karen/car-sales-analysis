import pandas as pd
import plotly.express as px
import streamlit as st
        
st.header('Análise exploratória de dados sobre vendas de carros.')

car_data = pd.read_csv('vehicles.csv') # lendo os dados
hist_button = st.button('Criar histograma') # criar um botão
        
if hist_button: # se o botão for clicado
            # escrever uma mensagem
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
            
            # criar um histograma
    fig = px.histogram(car_data, x="odometer")
        
            # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)


dispersao_button = st.button('Criar Gráfico de Dispersão')
if dispersao_button:
    st.write('Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')
    figs = px.scatter(car_data, x="odometer", y="price") 
    st.plotly_chart(figs, use_container_width=True)