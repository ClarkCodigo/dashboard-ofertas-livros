"""
Dashboard de Livros: app Streamlit.
"""

import streamlit as st
import dados
livros = dados.ler_livros()
quantia = len(dados.ler_livros())
media_preco = dados.calculo_media(livros)
estrelas = dados.quantidade_estrelas(livros)

st.set_page_config(layout="wide")
st.title("📚 Dashboard de Livros")
st.write("Se você está vendo esta página, o seu ambiente está pronto! 🎉")

col1, col2, col3 = st.columns(3)
col1.metric("Quantidade de livros", quantia)
col2.metric("Preço médio", f"£{media_preco:.2f}")
col3.metric("Livros cinco estrelas", estrelas)


st.dataframe(livros)