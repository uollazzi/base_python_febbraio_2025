from libri import Libro, Libreria

libro1 = Libro("Il Signore degli Anelli", "Tolkien", 1980)
libro2 = Libro("Dune", "Frank Herbert", 1980)
# print(libro1.desctizione())

libreria_salotto = Libreria("Libreria Salotto")
libreria_salotto.aggiungi_libro(libro1)
libreria_salotto.mostra_libri()

libreria_cucina = Libreria("Libreria Bianca Cucina")
libreria_cucina.aggiungi_libro(libro2)
libreria_cucina.mostra_libri()
