import os

file_esempio = "esempio.txt"

if os.path.exists(file_esempio):
    with open(file_esempio, "r") as file:
        testo = file.read()
        print(testo)
else:
    print(f"Il file {file_esempio} non esiste.")

with open(file_esempio, "w") as file:
    file.write("Ciao\n")
    file.write("sono")

os.remove(file_esempio)

paths = os.listdir(
    "C:\\Users\\dillo\\Il mio Drive\\Lavoro\\LABFORTRAINING\\CORSO PYTHON\\2025_febbraio_sera\\base\\data"
)

print(paths)

print(os.path.isdir("cicli.py"))

if not os.path.exists("data/gigi"):
    os.mkdir("data/gigi")

print(os.path.getmtime("data/gigi"))
