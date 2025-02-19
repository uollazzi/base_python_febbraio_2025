bici = {
    "nome": "BMX 200",
    "marca": "Bianchi",
    "prezzo": 1400,
    "inVendita": True,
    "taglie": [39, 67, 89, 41, 56],
    "colori": ["rosso", "giallo", "blu"],
    "categoria": {"codice": "BDC", "nome": "Bici da Corsa"},
    "disp": [
        {
            "magazzino": "Magazzino 1",
            "qta": 2,
            "indirizzo": {"via": "Pippo", "civico": "4", "citta": "ROMA (RM)"},
        },
        {
            "magazzino": "Magazzino 2",
            "qta": 3,
            "indirizzo": {"via": "Paperino", "civico": "445", "citta": "ROMA (RM)"},
        },
    ],
}

# stampare:
# 1 nome del prodotto
# 2 taglia più grande (hint: ciclo for)
# 3 L'indirizzo del Magazzino 2 nel formato seguente: Via Paperino, 445 - ROMA (RM)
# 4 Stmapare il totale delle biciclette in tutti i magazzini (5)  (hint: ciclo for)
print(bici["nome"])
print(max(bici["taglie"]))

m = bici["disp"][1]["indirizzo"]
print(f"{m["via"]}, {m["civico"]} - {m["citta"]}")

tot = 0
for mag in bici["disp"]:
    tot += mag["qta"]

print(tot)
