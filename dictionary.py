auto = {"marca": "Fiat", "modello": "Panda", "anno": 1990}

print(auto)

# accesso alle caratteristiche
print(auto["modello"])

auto["anno"] = 1991

print(auto)

ford = {
    "marca": "Ford",
    "anno": 1985,
    "elettrica": False,
    "colori": ["giallo", "nero", "bianco"],
}

colore = ford["colori"][1]
print(colore)

for colore in ford["colori"]:
    print(colore)

gianni = {"nome": "Gianni", "eta": 56, "moglie": {"nome": "Luisa", "eta": 50}}

# quanti anni ha la moglie di gianni
print(gianni["moglie"]["eta"])
print(type(gianni["moglie"]["eta"]))

pino = {"nome": "Pino", "anni": 34}

invitati_alla_festa = [
    {"nome": "Luca", "eta": 23},
    {"nome": "Paolo", "eta": 67},
    pino,
]

for invitato in invitati_alla_festa:
    print(invitato["nome"])
