from datetime import datetime

# OOP - Object Oriented Programming (Programmazione Orientata agli Oggetti)

# classe => è un progetto (o uno stampo con il quale creare gli oggetti)
# oggetto => è un qualcosa creato a partire da una classe
# creare un oggetto da una classe => istanziare


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


mario = Utente("Mario", 45)  # istanzio l'oggetto mario dalla classe Utente
gigi = Utente("Gigi", 23)

print(mario.nome)
print(gigi.nome)

mario.corri()
gigi.corri()

print(gigi.eta)

anna = Utente("Anna", 21)
anna.corri()

nascita = datetime(1976, 1, 20)
nascita.timestamp()
