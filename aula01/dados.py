"""Leitura dos arquivos CSV do projeto."""
from pathlib import Path
import csv
# Pasta onde este arquivo .py está. Assim o programa encontra o CSV
# mesmo quando é executado a partir de outra pasta (como no Streamlit Cloud).

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


if __name__ == "__main__":
    livros = ler_livros()   
    print(f"A quantidade de livros da coleção e de {len(livros)} livros.")



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
