a = "Ciao mondo!"

# trattare una stringa come una list di caratteri
# a = ["C", "i", "a", "o", " ", "m", "o", "n", "d", "o", "!"]
iniziale = a[0]
print(iniziale)

finale = a[-1]
print(finale)

print(a[:4])

numero_caratteri = len(a)
print(numero_caratteri)

txt = "ciao sono mario e ho 56 anni"
esiste_mario = "Mari" in txt
print(esiste_mario)

# trasformazione
print(a.upper())
print(a.lower())

c = "   Ciao gente    "
print(c.strip())  # rimuove spazi iniziali e finali

print(
    a.replace("o", "J")
)  # converti tutte le o in J nella string contenuta nella variabile z

c = "Via Indipendenza, 3, 12345, Roma (RM)"

stringa_divisa = c.split(",")
print(stringa_divisa)

# finestra sul futuro
# x = a.upper()
# y = x.replace("C", "W")
# z = y.split(" ")

# print(a.upper().replace("C", "W").split(" "))

for pezzo in stringa_divisa:
    print(pezzo.strip())

# concatenazione di stringhe
a = "Ciao"
b = "Mondo"

# Ciao Mondo!
c = a + " " + b + "!"
print(c)

qta = 9
codice = "XYZ123"
prezzo = 9.99

print(codice + str(qta))

# "Voglio 9 pezzi del prodotto con codice XYZ123 per 9.99 euro."
ordine = "Voglio {} pezzi del prodotto con codice {} per {} euro."
print(ordine.format(qta, codice, prezzo))

# f strings
ordine_completo = (
    f"Voglio {qta} pezzi del prodotto con codice {codice} per {prezzo} euro."
)
print(ordine_completo)

# escape
txt = 'Siamo "Quelli bravi"'
txt = 'Siamo "Quelli bravi"'

txt = """
Ciao
sono io

Arrivederci
"""

txt = """ciao"""
