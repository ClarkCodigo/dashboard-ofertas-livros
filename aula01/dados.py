"""Leitura dos arquivos CSV do projeto."""
from pathlib import Path
import csv
# Pasta onde este arquivo .py está. Assim o programa encontra o CSV
# mesmo quando é executado a partir de outra pasta (como no Streamlit Cloud).

PASTA = Path(__file__).parent
CAMINHO_LIVROS = PASTA / "livros.csv"

def ler_livros_v3():
    try:
        with open("livros.csv", "r", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)
            for linha in leitor:
                print(linha)
    except FileNotFoundError:
        print("O arquivo.csv não foi encontrado nessa aula")
    except Expection as error:
        print("Algum erro aconteceu na leitura desse arquivo")


def ler_livros_v2():
    try:
        with open("livros.csv", "r", encoding="utf-8") as arquivo:
            print(arquivo.readline())
    except FileNotFoundError:
        print("O arquivo.csv não foi encontrado nessa aula")
    except Expection as error:
        print("Algum erro aconteceu na leitura desse arquivo")

def ler_livros():
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

ler_livros_v3()
