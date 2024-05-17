import requests
from bs4 import BeautifulSoup
import pandas as pd
import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Função para raspar notícias
def scrape_news(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    articles = soup.find_all('article')
    news_data = []
    for article in articles:
        title = article.find('h2').text
        summary = article.find('p').text
        link = article.find('a')['href']
        news_data.append({'title': title, 'summary': summary, 'link': link})
    return pd.DataFrame(news_data)

# URLs de exemplo de sites de tecnologia
techcrunch_url = 'https://techcrunch.com/'
theverge_url = 'https://www.theverge.com/tech'

# Coletar dados
st.title('Análise de Notícias de Tecnologia')
source = st.selectbox('Selecione a Fonte de Notícias', ['TechCrunch', 'The Verge'])
if source == 'TechCrunch':
    df = scrape_news(techcrunch_url)
else:
    df = scrape_news(theverge_url)

# Mostrar as notícias
st.subheader('Notícias Recentes')
for index, row in df.iterrows():
    st.markdown(f"### [{row['title']}]({row['link']})")
    st.write(row['summary'])

# Análise de Palavras-chave
st.subheader('Análise de Palavras-chave')
text = ' '.join(df['title'].tolist())
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
st.pyplot(plt)
