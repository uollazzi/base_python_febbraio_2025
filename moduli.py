# importare tutto il contenuto di un modulo
import mio_modulo
import datetime

mio_modulo.saluta("Mario")

print(mio_modulo.somma(4, 5))

gigi = mio_modulo.Utente("Gigi", 67)

# importare tutto il contenuto di un modulo con alias
import mio_modulo as mm

# importare selettivamente
from mio_modulo import Utente, somma

pippo = Utente("Pippo", 23)

# importare tutto senza prefisso
from datetime import *

# pacchetti
import mio_pacchetto.modulo1 as m1
