import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def load_data():
    df = pd.read_csv('the_oscar_award.csv')
    return df

df = load_data()

st.title("Visualização de Indicações ao Oscar")

nome = st.text_input("Digite o nome do ator(a), diretor(a), produtor(a):")

if nome:
    df_filtrado = df[df['Nome'].str.contains(nome, case=False, na=False)]
    
    if not df_filtrado.empty:
        indicacoes_por_ano = df_filtrado['Ano'].value_counts().sort_index()

        fig, ax = plt.subplots()
        indicacoes_por_ano.plot(kind='bar', ax=ax)
        ax.set_title(f'Número de Indicações ao Oscar para {nome}')
        ax.set_xlabel('Ano')
        ax.set_ylabel('Número de Indicações')

        st.pyplot(fig)
    else:
        st.write(f'Nenhuma indicação encontrada para "{nome}".')
else:
    st.write("Por favor, insira um nome para buscar.")
