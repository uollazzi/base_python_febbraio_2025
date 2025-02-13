# una funzione è un blocco di codice pensato per essere ripetuto
def mia_funzione():
    print("===================")
    print("Ciao dalla funzione")
    print("===================")


for n in range(5):
    mia_funzione()


# parametro (argomento) della funzione
def saluta(nome):
    print(f"Ciao {nome.upper()}")


saluta("Gigi")
saluta("Mario")


# parametri multipli (POSIZIONALI)
def presentati(nome, cognome, anni):
    mag_min = ""

    if anni >= 18:
        mag_min = "maggiorenne"
    else:
        mag_min = "minorenne"

    print(f"Ciao sono {nome} {cognome} e sono {mag_min}")


presentati("Mario", "Verdi", 89)
presentati(anni=45, nome="Gigi", cognome="Riva")


# torna un valore che posso mettere in una variabile e riutilizzare
def somma(n1, n2):
    return n1 + n2


risultato = somma(3, 5)
print(f"Il risultato è: {risultato}")
print(f"Il risultato al quadrato è: {risultato**2}")
print(f"Il risultato è: {somma(4,5)}")

eta = print("Ciao")
print(eta)  # None

print(somma(8, 9))


# parametri default/opzionali
def spedisci(prodotto, paese="Italia"):
    print(f"Il prodotto {prodotto} è stato spedito in {paese}")


spedisci("Bici", "Italia")
spedisci("Ciabatte")
spedisci("Pantaloni", "Spagna")


# *args
def somma_multipla(*numeri):
    totale = 0

    for n in numeri:
        totale += n

    return totale


print(somma_multipla(3, 4, 5))
print(somma_multipla(3, 4, 65, 45, 89))


# print esempio eclatante
print("Ciao", "Matteo", "Saluti", 89, True)
