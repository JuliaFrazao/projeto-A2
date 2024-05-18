import requests
from bs4 import BeautifulSoup
import pandas as pd
import streamlit as st

# Função para raspar as avaliações dos produtos
def scrape_reviews(product_name):
    # Substituir espaços por hífens para criar a URL de pesquisa
    query = product_name.replace(' ', '-')
    url = f"https://www.sephora.com.br/{query}"

    # Fazer a requisição HTTP para a página do produto
    response = requests.get(url)
    if response.status_code != 200:
        st.error("Produto não encontrado ou não há avaliações disponíveis.")
        return None

    soup = BeautifulSoup(response.content, 'html.parser')

    # Encontrar as avaliações na página
    reviews_section = soup.find_all('div', class_='bazaarvoice-container')
    if not reviews_section:
        st.error("Não foram encontradas avaliações para este produto.")
        return None

    reviews = []
    for review in reviews_section:
        try:
            rating = review.find('span', class_='bv-rating-stars-container').text.strip()
            title = review.find('h3', class_='bv-content-title').text.strip()
            content = review.find('div', class_='bv-content-summary-body-text').text.strip()
            reviews.append({
                'Título': title,
                'Avaliação': rating,
                'Conteúdo': content
            })
        except AttributeError:
            continue

    return pd.DataFrame(reviews)

# Interface do Streamlit
st.title('Avaliações de Produtos de Maquiagem e Beleza - Sephora Brasil')

product_name = st.text_input('Digite o nome do produto que deseja ver as avaliações:', '')

if st.button('Buscar Avaliações'):
    if product_name:
        reviews_df = scrape_reviews(product_name)
        if reviews_df is not None and not reviews_df.empty:
            st.subheader(f'Avaliações para "{product_name}"')
            st.dataframe(reviews_df)
        else:
            st.info("Nenhuma avaliação encontrada para o produto especificado.")
    else:
        st.warning("Por favor, insira o nome de um produto.")

# Rodar o código Streamlit no terminal
# streamlit run nome_do_arquivo.py
