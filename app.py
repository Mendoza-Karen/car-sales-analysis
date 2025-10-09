import pandas as pd
import plotly.express as px
import streamlit as st

# O h1 define que o markdown representa o Titulo(cabeçalho)
st.markdown("<h1 style='color: #ff9bb8;text-align: center;'>Análise exploratória de dados sobre anúncios de carros:</h1>", unsafe_allow_html=True)

#lendo o dataframe
car_data = pd.read_csv('vehicles.csv') 

#exibindo o dataframe na aplicação web, usando o streamlit.
st.dataframe(car_data) 

# p = significa um texto simples, com ajuda do html mudei a cor.
# unsafe_allow_html=True, esse argumento permite usar HTML diretamente na aplicação.
st.markdown("<p style='color: #fed7e2;'>Aperte o botão para criar um histograma baseado nos valores da quilometragem dos carros:</p>", unsafe_allow_html=True)  

# usando HTML para definir a cor de todos os botões.
st.markdown("""
    <style>
    .stButton>button {
        background-color:#ff9bb8;  
        color: white;               
        height: 50px;  }
    </style>
""", unsafe_allow_html=True)

#Criando um botão e um histograma.
hist_button = st.button('Criar histograma')
if hist_button:     
    fig = px.histogram(car_data, x="odometer")
    # .plotly_chart, serve para exibir o gráfico na aplicação.
    st.plotly_chart(fig, use_container_width=True)

st.markdown("<p style='color:#fed7e2;'>Aperte o botão para criar um gráfico de dispersão da relação entre a quilometragem e o preço dos carros:</p>", unsafe_allow_html=True) 

#Criando um botão e um gráfico de dispersão.
dispersao_button = st.button('Criar Gráfico de Dispersão')
if dispersao_button:
    figs = px.scatter(car_data, x="odometer", y="price",color_discrete_sequence=['pink']) 
    st.plotly_chart(figs, use_container_width=True)

#Criando um gráfico pizza.
fig4 = px.pie(car_data, names='fuel', title='Distribuição dos tipos de combustível:',color_discrete_sequence=['#FF69B4', '#00BFFF', 'red','#FFA500','#9D00FF'  ])
st.plotly_chart(fig4)

#agrupamento e criação da um grafico de barras para saber a médias dos preços baseado nas condições do carro.
receita = car_data.groupby('condition')['price'].mean().reset_index()
fig3 = px.bar(receita, x = 'condition', y='price', title='Preço médio baseado na condição dos carros:',color_discrete_sequence=['pink'])
st.plotly_chart(fig3)

#agrupamento e criação da um grafico de barras para saber a médias dos preços baseado nos modelos de carros.
model_price = car_data.groupby('model', as_index=False)['price'].mean()
fig5 = px.bar(model_price, x='model', y='price', title='Preço médio baseado nos modelos dos carros:',color_discrete_sequence=['pink'])
st.plotly_chart(fig5)