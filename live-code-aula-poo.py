"""
Codigo Harry Potter - Chapeu seletor POO
"""

class Estudante:
    # Construtor
    def __init__(self, nome, casa):
        if not nome:
            raise ValueError

        if casa not in ["Grifinória","Sonserina","Lufa-lufa","Corvinal"]:
            raise ValueError("Casa Invalida")

        self.nome = nome
        self.casa = casa

    # Renderização do objeto
    def __str__(self):
        return f"O bruxo {self.nome} pertence a casa {self.casa}, e seu patrono e {self.get_patrono()}"
    
    #Metodo (Instance Method)
    def get_patrono(self):
        match self.nome:
            case "Roni":
                return "Cachorro"
            case "Hermione":
                return "Lontra"
            case "Harry Potter":
                return "Cervo"
        return "Indefinido"
            


def main():
    estudante = get_estudante()
    print(estudante)

    # print(f"O bruxo {estudante.nome} pertence a casa {estudante.casa}")


def get_estudante():

    nome = input ("Nome do bruxo: ")
    casa = input ("Casa: ")

    estudante = Estudante(nome, casa)
    return estudante

if __name__  == "__main__":
    main()