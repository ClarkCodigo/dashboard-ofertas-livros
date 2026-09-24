"""Leitura dos arquivos CSV do projeto."""
from pathlib import Path
import csv

PASTA = Path(__file__).parent
CAMINHO_LIVROS = PASTA / "livros.csv"

def ler_livros():
    livros=[]
    try:
        with open(CAMINHO_LIVROS, "r", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)
            for linha in leitor:
                livros.append(linha)
    except FileNotFoundError:
        print("O arquivo.csv não foi encontrado nessa aula")
    except Expection as error:
        print("Algum erro aconteceu na leitura desse arquivo")
    return livros

def calculo_media(livros):
    soma: float = 0
    for livro in livros:
        preco_original: str         = livro["preco"]
        preco_original_limpo: str   =  preco_original.replace("£","")
        preco_num: float            = float(preco_original_limpo)
        soma += preco_num
    preco_medio: float = soma /len(livros)
    return preco_medio

def quantidade_estrelas(livros):
    estrelas: int = 0
    for livro in livros:
        not_limpa: str = livro["nota"].lower().strip()
        if not_limpa == "five":
            estrelas = estrelas + 1
    return estrelas

#area de testes
if __name__ == "__main__":
    livros = ler_livros() 
    # print(f"A quantidade de livros da coleção e de {len(livros)} livros.")
    # preco_medio:float = calculo_media(livros)
    # print (f"Preço medio £{preco_medio:.2f}")
    # cinco_estrelas = quantidade_estrelas(livros)
    # print(f"Quantidade cinco estrelas: {cinco_estrelas}")

#versoes basicas
def ler_livros_v2():
    try:
        with open("livros.csv", "r", encoding="utf-8") as arquivo:
            print(arquivo.readline())
    except FileNotFoundError:
        print("O arquivo.csv não foi encontrado nessa aula")
    except Expection as error:
        print("Algum erro aconteceu na leitura desse arquivo")

def ler_livros_v1():
    arquivo = None
    try:
        arquivo = open("livros.csv", "r", encoding="utf-8")
        print(arquivo.readline())
    except FileNotFoundError:
        print("O arquivo.csv não foi encontrado nessa aula")
    except Expection as error:
        print("Algum erro aconteceu na leitura desse arquivo")
    finally:
        if arquivo is not None:
            arquivo.close()
