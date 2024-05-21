import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Carregar o dataset
@st.cache
def load_data():
    # Substitua 'oscars_dataset.csv' pelo caminho para o seu arquivo CSV
    df = pd.read_csv('the_oscar_award.csv')
    return df

# Carregar os dados
df = load_data()

# Título do aplicativo
st.title("Visualização de Indicações ao Oscar")

# Entrada do usuário
nome = st.text_input("Digite o nome do ator(a), diretor(a), produtor(a):")

# Filtrar o dataset pelo nome inserido
if nome:
    df_filtrado = df[df['Nome'].str.contains(nome, case=False, na=False)]
    
    if not df_filtrado.empty:
        # Contar o número de indicações por ano
        indicacoes_por_ano = df_filtrado['Ano'].value_counts().sort_index()

        # Criar o gráfico
        fig, ax = plt.subplots()
        indicacoes_por_ano.plot(kind='bar', ax=ax)
        ax.set_title(f'Número de Indicações ao Oscar para {nome}')
        ax.set_xlabel('Ano')
        ax.set_ylabel('Número de Indicações')

        # Exibir o gráfico no Streamlit
        st.pyplot(fig)
    else:
        st.write(f'Nenhuma indicação encontrada para "{nome}".')
else:
    st.write("Por favor, insira um nome para buscar.")
