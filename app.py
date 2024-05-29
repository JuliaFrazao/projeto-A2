import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados do CSV
@st.cache
def load_data():
    data = pd.read_csv('movies.csv')
    return data

data = load_data()

st.title("Informações sobre Filmes por Ator/Atriz")

# Entrada do usuário para o nome do ator/atriz
actor_name = st.text_input("Digite o nome do ator/atriz:")

if actor_name:
    # Filtrar os dados pelo nome do ator/atriz
    actor_data = data[data['star'] == actor_name]
    
    if not actor_data.empty:
        st.write(f"Filmes com {actor_name}:")
        st.write(actor_data['name'])
        
        # Opções para o usuário escolher
        option = st.selectbox("Escolha uma opção:", ("Anos de atuação", "Gêneros de filmes"))
        
        if option == "Anos de atuação":
            years = actor_data['year'].value_counts().sort_index()
            st.write("Anos de atuação:")
            st.bar_chart(years)
        
        elif option == "Gêneros de filmes":
            genres = actor_data['genre'].value_counts()
            st.write("Gêneros de filmes mais atuados:")
            st.bar_chart(genres)
    else:
        st.write("Nenhum filme encontrado para o ator/atriz especificado.")

