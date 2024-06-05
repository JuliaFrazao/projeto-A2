import streamlit as st
import pandas as pd
import altair as alt

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
O objetivo do aplicativo é servir como um buscador de informações sobre a indústria cinematográfica americana, 
contendo 7512 filmes. Divirta-se!
""")

# Aplicar CSS personalizado
st.markdown(
    """
    <style>
    .stApp {
        background: url('https://raw.githubusercontent.com/JuliaFrazao/projeto-A2/main/cortina%20vermelha.jpg') no-repeat center center fixed;
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)

col1, col2 = st.columns([1, 6])

with col1:
    st.image(image_url, width=90)

with col2:
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
            st.write(actor_data[['name']].reset_index(drop=True))
            
            # Opções para o usuário escolher
            option = st.selectbox("Escolha uma opção:", ("Anos de atuação", "Gêneros de filmes"))
            
            if option == "Anos de atuação":
                years = actor_data['year'].value_counts().sort_index().reset_index()
                years.columns = ['year', 'count']
                st.write("Anos de atuação:")
                
                # Criar o gráfico com a cor vermelha usando Altair
                chart = alt.Chart(years).mark_bar(color='red').encode(
                    x='year:O',
                    y='count:Q'
                )
                st.altair_chart(chart, use_container_width=True)
            
            elif option == "Gêneros de filmes":
                genres = actor_data['genre'].value_counts().reset_index()
                genres.columns = ['genre', 'count']
                st.write("Gêneros de filmes mais atuados:")
                
                # Criar o gráfico com a cor vermelha usando Altair
                chart = alt.Chart(genres).mark_bar(color='red').encode(
                    x='genre:O',
                    y='count:Q'
                )
                st.altair_chart(chart, use_container_width=True)
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
                budgets = director_data[['name', 'budget']].set_index('name').reset_index()
                st.write("Orçamento dos filmes:")
                
                # Criar o gráfico de orçamento dos filmes com a cor vermelha usando Altair
                chart = alt.Chart(budgets).mark_bar(color='red').encode(
                    x='name:O',
                    y='budget:Q'
                )
                st.altair_chart(chart, use_container_width=True)
            
            elif option == "Estúdio de cinema":
                company = director_data[['name', 'company']].set_index('name')
                st.write("Estúdios de cinema que produziram os filmes:")
                st.table(company.reset_index())
        else:
            st.write("Nenhum filme encontrado para o diretor/diretora especificado.")
