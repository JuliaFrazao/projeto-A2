import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados do CSV
@st.cache
def load_data():
    data = pd.read_csv('movies.csv')
    return data

data = load_data()

# Adicionar a descrição na barra lateral
st.sidebar.title("Sobre o Aplicativo")
st.sidebar.info("""
O aplicativo tem como objetivo servir como um buscador de informações sobre a indústria cinematográfica americana, 
contendo 7512 filmes lançados entre 1986 e 2016. Divirta-se!
""")

st.title("Informações sobre Filmes de Hollywood")

# Entrada do usuário para escolher entre ator/atriz e diretor/diretora
search_option = st.selectbox("Você quer buscar informações sobre:", ("Ator/Atriz", "Diretor/Diretora"))

if search_option == "Ator/Atriz":
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

elif search_option == "Diretor/Diretora":
    director_name = st.text_input("Digite o nome do diretor/diretora:")

    if director_name:
        # Filtrar os dados pelo nome do diretor/diretora
        director_data = data[data['director'] == director_name]
        
        if not director_data.empty:
            st.write(f"Filmes dirigidos por {director_name}:")
            st.write(director_data['name'])
            
            # Opções para o usuário escolher
            option = st.selectbox("Escolha uma opção:", ("Orçamento dos filmes", "Estúdio de cinema"))

            if option == "Orçamento dos filmes":
                budgets = director_data[['title', 'budget']].set_index('name')
                st.write("Orçamento dos filmes:")
                st.bar_chart(budgets)
            
            elif option == "Estúdio de cinema":
                company = director_data['company'].value_counts()
                st.write("Estúdios de cinema que produziram os filmes:")
                st.bar_chart(company)
        else:
            st.write("Nenhum filme encontrado para o diretor/diretora especificado.")

