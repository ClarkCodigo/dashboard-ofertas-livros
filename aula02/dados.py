"""Leitura dos arquivos CSV do projeto."""

import csv
from pathlib import Path

# Pasta onde este arquivo .py está. Assim o programa encontra o CSV
# mesmo quando é executado a partir de outra pasta (como no Streamlit Cloud).
PASTA = Path(__file__).parent
CAMINHO_LIVROS = PASTA / "livros.csv"

def ler_livros():
    """Lê o CSV de livros e devolve uma lista de dicionários.

    Os valores vêm do jeito que estão no arquivo, ou seja, como texto:
    {"titulo": "Sharp Objects", "preco": "£47.82", "nota": "Four", ...}
    """
    livros = []
    try:
        with open(CAMINHO_LIVROS, "r", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)
            for linha in leitor:
                livros.append(linha)
    except FileNotFoundError:
        print("O arquivo livros.csv não foi encontrado")
    except Exception as error:
        print("Algum erro aconteceu na leitura do arquivo", error)

    return livros


def calcular_preco_medio(livros):
    """Soma os preços de todos os livros e divide pelo total.

    O preço vem como texto ("£51.77"): removemos o "£" e convertemos com float.
    """
    soma = 0
    for livro in livros:
    #     preco_original: str = livro["preco"]
    #     preco_original_limpo: str = preco_original.replace("£", "")
    #     preco_num: float = float(preco_original_limpo)
        soma += livro["preco"]

    preco_medio: float = soma / len(livros)
    return preco_medio

def contar_cinco_estrelas(livros):
    """Conta quantos livros têm a nota máxima. A nota vem como texto ("Five")."""
    contador: int = 0
    for livro in livros:
        # nota_limpa: str = livro["nota"].lower().strip()
        if livro["nota"] == 5:
            contador += 1

    return contador


def encontrar_mais_caro(livros):
    """Devolve o livro de maior preço. O preço vem como texto ("£51.77")."""
    mais_caro = livros[0]
    for livro in livros:
        # preco = float(livro["preco"].replace("£", ""))
        # preco_mais_caro = float(mais_caro["preco"].replace("£", ""))
        if livro["preco"] > mais_caro["preco"]:
            mais_caro = livro
    return mais_caro


def converte_preco(preco):
    ''' Remove o sinal de libra dos preços '''
    return float(preco.replace("£", ""))


def convert_nota(nota):
    ''' Troca string por valor numero inteiro '''
    match nota:
        case "Five":
            return 5
        case "Four":
            return 4
        case "Tree":
            return 3
        case "Two":
            return 2
        case _:
            return 1


def preparar_livros(linhas):
    livros = []
    for linha in linhas:
        livro = {
            "titulo":   linha["titulo"],
            "preco":    converte_preco(linha["preco"]),
            "categoria":linha["categoria"],
            "nota":    convert_nota(linha["nota"]),
            "url":      linha["url"]
        }
        livros.append(livro)
    return livros

def carregar_livros():
    return preparar_livros(ler_livros())


if __name__ == "__main__":
    livros = ler_livros()
    livro_teste= preparar_livros(livros)

    print(len(livro_teste))
    # livros_convertidos = preparar_livros(livros)

    # print(f"Livro o:{livros[0]}")
    # print(f"Livro p:{livros_convertidos[0]}")

    # print(f"{len(livros)} livros carregados")
    # print("Primeiro livro:", livros[0])
