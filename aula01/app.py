"""
Dashboard de Livros: app Streamlit.
"""

import streamlit as st
import dados

# variaveis chamadas
livros      = dados.ler_livros()
quantia     = len(dados.ler_livros())
media_preco = dados.calculo_media(livros)
estrelas    = dados.quantidade_estrelas(livros)
livro_mais_caro = dados.preco_mais_caro(livros)

st.set_page_config(layout="wide") #define o estilo da pagina
st.title("📚 Dashboard de Livros")
# st.write("Se você está vendo esta página, o seu ambiente está pronto! 🎉")

col1, col2, col3, col4 = st.columns(4) #define a separação por coluna
col1.metric("Quantidade de livros", quantia)
col2.metric("Preço médio", f"£{media_preco:.2f}")
col3.metric("Livros cinco estrelas", estrelas)
col4.metric("Livro mais caro", f"£{livro_mais_caro:.2f}")

#incluir com st.caption
#chamda de dados formatados
st.dataframe(livros)