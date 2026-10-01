"""Dashboard de Livros: app Streamlit.
"""

import streamlit as st

import dados

def monstasr_tabela(livros):
    tabela = []
    for livro in livros:
        linha = {
            "Titulo":   livro["titulo"],
            "Categoria":livro["categoria"],
            "Nota":     livro["nota"] * "✩",
            "Titulo":   livro["titulo"],
            "Preço":    f"£{livro["preco"]:.2f}",
            "Faixa": classificar_preco(livro["preco"])
        }
        tabela.append(linha)
    return tabela

def classificar_preco(preco):
    """ Define a categoria de preço """

    if preco < 20:
        return "Barato"
    elif preco <= 40:
        return "Medio"
    else:
        return "Caro"
    
def contar_por_faixa_dic(livros):
    """ Contagem e categorização em um dicionario """

    contagem = {}
    for livro in livros:
        faixa = classificar_preco(livro["preco"])

        # if faixa in contagem:
        #     contagem[faixa] = contagem[faixa] + 1
        # else:
        #     contagem[faixa] = 1

        #versao condicional ternario
        contagem[faixa] = contagem[faixa] + 1 if faixa in contagem else 1

    return contagem

def contar_por_faixa(livros):
    """ Indica a quantiade de livros por categoria """

    contar_baratos = 0
    contar_medios = 0
    contar_caros = 0

    for livro in livros:
        if classificar_preco(livro) == "Barato":
            contar_baratos +=1
        elif classificar_preco(livro) == "Medio":
            contar_medios +=1
        else:
            contar_caros +=1
            
    return contar_baratos, contar_medios, contar_caros

def main():
    st.set_page_config(page_title="Dashboard de Livros", page_icon="📚", layout="wide")
    st.title("📚 Dashboard de Livros")

    # livros_originais = dados.ler_livros()
    livros = dados.carregar_livros()
    tabela = monstasr_tabela(livros)

    col1, col2, col3, col4 = st.columns(4)
    qtd_livros = len(livros)
    col1.metric("Total de Livros", qtd_livros)

    preco_medio = dados.calcular_preco_medio(livros)
    col2.metric("Preço médio", f"£{preco_medio:.2f}")

    cinco_estrelas = dados.contar_cinco_estrelas(livros)
    col3.metric("Qtd. livros 5 Estrelas", cinco_estrelas)

    mais_caro = dados.encontrar_mais_caro(livros)
    col4.metric("Livro mais caro £", f"{mais_caro["preco"]}")
    col4.caption(mais_caro["titulo"])

    st.dataframe(tabela)


if __name__ == "__main__":
    main()
