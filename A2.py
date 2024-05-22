import streamlit as st
import pandas as pd

# Carregar o dataset
@st.cache
def load_data():
    # Substitua 'netflix_titles.csv' pelo caminho para o seu arquivo CSV
    df = pd.read_csv('NetFlix.csv')
    return df

# Carregar os dados
df = load_data()

# Título do aplicativo
st.title("Busca de Filmes e Séries da Netflix por Ator/Atriz")

# Entrada do usuário para o nome do ator/atriz
nome_ator = st.text_input("Digite o nome do ator ou atriz:")

# Filtrar o dataset pelo nome inserido
if nome_ator:
    df_filtrado = df[df['cast'].str.contains(nome_ator, case=False, na=False, regex=False)]
    
    if not df_filtrado.empty:
        st.write(f"Filmes e Séries com {nome_ator}:")
        st.dataframe(df_filtrado[['title', 'cast', 'type', 'country', 'release_year', 'rating']])
    else:
        st.write(f'Nenhum filme ou série encontrado com "{nome_ator}".')
else:
    st.write("Por favor, insira o nome de um ator ou atriz.")
