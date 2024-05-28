import streamlit as st
import pandas as pd

# Carregar o dataset
@st.cache
def load_data():
    df = pd.read_csv('movies.csv')
    return df

# Carregar os dados
df = load_data()

# Título do aplicativo
st.title("Buscador de atores e atrizes de Hollywood")

# Entrada do usuário para o nome do ator/atriz
nome_ator = st.text_input("Digite o nome do ator ou atriz:")

# Filtrar o dataset pelo nome inserido
if nome_ator:
    df_filtrado = df[df['star'].str.contains(nome_ator, case=False, na=False, regex=False)]
    
    if not df_filtrado.empty:
        st.write(f"Filmes e Séries com {nome_ator}:")
        st.dataframe(df_filtrado[['name', 'genre', 'year', 'country', 'star']])
    else:
        st.write(f'Nenhum filme encontrado com "{nome_ator}".')
else:
    st.write("Por favor, insira o nome de um ator ou atriz.")
