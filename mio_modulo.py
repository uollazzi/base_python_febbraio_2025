def saluta(nome):
    print("Ciao", nome)


def somma(x, y):
    return x + y


class Utente:
    # costruttore
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta
        print("Nuovo utente creato")

    def corri(self):
        if self.eta > 40:
            print(f"Sono {self.nome} e sono troppo vecchio per correre")
        else:
            print(f"Sono {self.nome}, ho {self.eta} anni e sto correndo")
