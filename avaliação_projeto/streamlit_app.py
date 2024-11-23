import streamlit as st
import pandas as pd
import requests
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Análise de Dados Superstore", layout="wide")

st.title("Análise Interativa de Dados Superstore")

data_file = st.file_uploader("Faça o upload do arquivo CSV", type=["csv"])

if data_file:
    data = pd.read_csv(data_file)
    data['Order_Date'] = pd.to_datetime(data['Order_Date'])
    data['Ship_Date'] = pd.to_datetime(data['Ship_Date'])
    data.fillna({'Postal_Code': 0}, inplace=True)

    st.write("### Visualização de Amostra dos Dados")
    st.write(data.head())

    st.write("### Estatísticas Básicas")
    st.write(data.describe())

    st.write("### Visualização de Dados")
    st.write("Selecione o tipo de gráfico desejado:")
    chart_type = st.selectbox("Tipo de gráfico", ["Histograma", "Gráfico de Dispersão", "Gráfico de Barras"])

    if chart_type == "Histograma":
        column = st.selectbox("Selecione a coluna", data.select_dtypes(include=['int64', 'float64']).columns)
        fig, ax = plt.subplots()
        sns.histplot(data[column], kde=True, ax=ax)
        st.pyplot(fig)

    elif chart_type == "Gráfico de Dispersão":
        x_column = st.selectbox("Selecione o eixo X", data.select_dtypes(include=['int64', 'float64']).columns)
        y_column = st.selectbox("Selecione o eixo Y", data.select_dtypes(include=['int64', 'float64']).columns)
        fig, ax = plt.subplots()
        sns.scatterplot(x=data[x_column], y=data[y_column], ax=ax)
        st.pyplot(fig)

    elif chart_type == "Gráfico de Barras":
        column = st.selectbox("Selecione a coluna categórica", data.select_dtypes(include=['object']).columns)
        fig, ax = plt.subplots()
        data[column].value_counts().plot(kind='bar', ax=ax)
        st.pyplot(fig)

    st.write("### Consultar API Flask")
    api_url = st.text_input("Insira a URL da API Flask", "http://localhost:5000")

    if st.button("Obter Estatísticas via API"):
        response = requests.get(f"{api_url}/api/statistics")
        if response.status_code == 200:
            st.json(response.json())
        else:
            st.error("Erro ao consultar a API.")

    record_id = st.number_input("Insira o ID do registro para consulta", min_value=0, step=1)
    if st.button("Obter Registro via API"):
        response = requests.get(f"{api_url}/api/record/{record_id}")
        if response.status_code == 200:
            st.json(response.json())
        else:
            st.error("Erro ao consultar a API.")
