# lista
# ordinate
# modificabili
# ammettono duplicati
# indicizzate (base 0)

frutta = ["mela", "banana", "pera"]
print(frutta)

# accedere all'elemento alla posizione 0 (primo elemento)
print(frutta[0])

frutta[0] = "fragola"
print(frutta)

# lista varia
lista2 = [1, "ciao", True]

# accesso agli elementi
frutta = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

print(frutta[2:5])
print(frutta[:5])
print(frutta[2:])
print(frutta[-1])
print(frutta[:-2])

print(frutta[1])
print(frutta[5])

f = [frutta[1], frutta[5]]
print(type(f))
print(f)

indice = frutta.index("kiwi")
print(indice)

# indice = frutta.index("pera")
print(indice)

esiste_pera = "pera" in frutta
print(esiste_pera)

# creare una variabile di nome fr che contiene una stringa con un frutto
# verificare che il valore della varaibile fr esista in frutta
# se esiste scrivere a terminale "[nome della frutta] trovato"
# altrimenti scrivere a terminale "[nome della frutta] non esiste"
# testare il tutto provando a cambiare il valore della variabile fr
fr = "mela"

if fr in frutta:
    print(fr + " trovato")
else:
    print(fr + " non esiste")


# aggiungere elementi alla lista
frutta.append("watermelon")
print(frutta)

frutta.insert(2, "ananas")
print(frutta)

# rimozione
frutta.remove("kiwi")
print(frutta)

frutta.pop()
print(frutta)

frutta.pop(2)
print(frutta)

# copia (riferimento)
f = frutta

print(frutta[0])
print(f[0])

frutta[0] = "prugna"

print(frutta[0])
print(f[0])

# copia (copia vera)
f = frutta.copy()

print("FINITO")
