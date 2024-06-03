import streamlit as st
import pandas as pd

image_url = "emoji.jpg"

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
contendo 7512 filmes. Divirta-se!
""")

st.markdown(
    """
    <div style="display: flex; align-items: center;">
        <h1 style="flex: 1;">Informações sobre Filmes de Hollywood</h1>
        <img src='emoji.jpg' width='60px'>
    </div>
    """, 
    unsafe_allow_html=True
)

# Entrada do usuário para escolher entre ator/atriz e diretor/diretora
search_option = st.selectbox("Você quer buscar informações sobre:", ("Ator/Atriz", "Diretor/Diretora"))

if search_option == "Ator/Atriz":
    actor_name = st.text_input("Digite o nome do ator/atriz:")

    if actor_name:
        # Filtrar os dados pelo nome do ator/atriz
        actor_data = data[data['star'] == actor_name]
        
        if not actor_data.empty:
            st.write(f"Filmes com {actor_name}:")
            st.write(actor_data[['name']].reset_index(drop=True))
            
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
            st.write(director_data[['name']].reset_index(drop=True))
            
            # Opções para o usuário escolher
            option = st.selectbox("Escolha uma opção:", ("Orçamento dos filmes", "Estúdio de cinema"))

            if option == "Orçamento dos filmes":
                budgets = director_data[['name', 'budget']].set_index('name')
                st.write("Orçamento dos filmes:")
                st.table(budgets)
            
            elif option == "Estúdio de cinema":
                company = director_data[['name', 'company']].set_index('name')
                st.write("Estúdios de cinema que produziram os filmes:")
                st.table(company.reset_index())
        else:
            st.write("Nenhum filme encontrado para o diretor/diretora especificado.")

