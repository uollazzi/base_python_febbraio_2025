class Libro:
    def __init__(self, titolo, autore, anno_pubblicazione):
        self.titolo = titolo
        self.autore = autore
        self.anno_pubblicazione = anno_pubblicazione

    def desctizione(self):
        return f"{self.titolo} di {self.autore} pubblicato il {self.anno_pubblicazione}"


# Libreria / LibriManager
class Libreria:
    def __init__(self, nome):
        self.libri = []
        self.nome = nome

    def aggiungi_libro(self, libro):
        if libro.titolo == "":
            print("Attenzione specificare un titolo")
        else:
            self.libri.append(libro)
            print(f"{libro.titolo} aggiunto con successo.")

    def mostra_libri(self):
        print(f"Elenco libri di {self.nome}:")
        if len(self.libri) == 0:
            print("La libreria è vuota")
        else:
            for l in self.libri:
                print("-", l.titolo)
        print("----------")
