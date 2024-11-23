#Participantes: Letícia Vitoria de Souza, Guilherme Garcia e Christiane Henck

\# Orders Analysis Project

Desenvolvimento de uma aplicação de análise de dados integrada com Flask e Streamlit que permita a análise de pedidos para tirar insights.

A aplicação carrega e processa dados de pedidos, clientes e categorias de produtos, permitindo a visualização de tendências e consulta interativa..

\## Funcionalidades

Carregar e processar dados de um arquivo específico.

Utilizar widgets interativos para selecionar e filtrar informações.

Exibir análises de dados e visualizações para auxiliar na tomada de decisão.

Executar uma API local para fornecer dados e interações.

\## Estrutura do Projeto e ordem dos códigos

├── avaliação\_projeto

│   ├── loader.py       # Script de carregamento e pré-processamento dos dados

│   ├── analysis.py     # Script de análise de dados com funções para visualização

│   ├── app.py               # Script da API para fornecer endpoints de dados

│   ├── streamlit\_app.py               # Script principal que executa a aplicação Streamlit

│   ├── executar.py               # Script para rodar Flask e Streamlit simultaneamente.

│   └── README.md            # Documento explicativo do projeto

\## Instalação

\## Instale as dependências:

Rodar no prompt pip install -r requirements.txt

\### Requirements

- Python 3.3+
- Pandas
- Flask
- Streamlit
- Matplotlib

\## Exemplo de Uso

A aplicação apresenta uma interface para análise dos dados pedidos, permitindo a filtragem e seleção de métricas específicas. Ao escolher uma métrica, a aplicação gera visualizações interativas que facilitam o entendimento dos dados.

Informações do Dataset:

- Total de linhas: 9800
- Total de colunas: 16
- Nomes das colunas: ['Order\_ID', 'Order\_Date', 'Ship\_Date', 'Ship\_Mode', 'Customer\_ID', 'Customer\_Name', 'Segment', 'Country', 'City', 'State', 'Postal\_Code', 'Region', 'Product\_ID', 'Category', 'Sub-Category', 'Product\_Name']

##Análises:

Volume por categoria e subcategoria

Popularidade de produtos

Tempo médio de entrega por categoria

Clientes mais frequentes

Sazonalidade nas vendas

Previsão de demanda por mês


