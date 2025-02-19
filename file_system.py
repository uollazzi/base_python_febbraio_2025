import os

# lettura file
# f = open("demo.txt")
# contenuto = f.read()
# print(contenuto)
# f.close()

with open("demo.txt") as f:
    contenuto = f.read()
    print(contenuto)

# mode
# r => read
# w => write
# a => append
with open("demo.txt", "rt", encoding="utf8") as f:
    contenuto = f.read()
    print(contenuto)


vendite = []
with open("sales.csv", "r") as sales:
    vendite = sales.readlines()
    print(vendite)

vendite.append("\n4;18/02/2024;Jeans")

with open("sales.csv", "wt") as sales:
    sales.writelines(vendite)

with open("sales.csv", "at") as sales:
    sales.write("\n5;19/02/2024;Scarpe")

# creazione automatica dei files che non esistono
with open("dummy_file.txt", "w") as d:
    d.write("ciao")

if os.path.exists("dummy_file.txt") == True:
    # rimozione file
    os.remove("dummy_file.txt")
    print("Il file dummy_file.txt è stato rimosso con successo.")
else:
    print("Il file dummy_file.txt non esiste.")

# cartelle
cartella_da_analizzare = "."
elenco_files_e_cartelle = os.listdir(cartella_da_analizzare)
print("====================================")
print(f"Elenco files e cartelle nella cartella {cartella_da_analizzare}")
for fc in elenco_files_e_cartelle:
    # is_dir = os.path.isdir(fc)
    # tipo = "[F]"

    # if is_dir:
    #     tipo = "[D]"

    # print(tipo, fc)

    print("[D]" if os.path.isdir(fc) else "[F]", fc)

# FUNZIONE RICORSIVA
# print("ùùùùùùùùùùùùùùùùùùùùùùù")

# # creare una cartella
# def analizza_cartella(cartella):
#     elenco_files_e_cartelle = os.listdir(cartella)
#     for fc in elenco_files_e_cartelle:
#         is_dir = os.path.isdir(fc)
#         tipo = "[F]"

#         if is_dir:
#             tipo = "[D]"
#             analizza_cartella(os.path.join(cartella, fc))

#         print(tipo, fc)


# analizza_cartella(".")

# crare una cartella
if not os.path.exists("sottocartella"):
    os.mkdir("sottocartella")

anni = [2018, 2019, 2021, 2022, 2023, 2024, 2025]
for anno in anni:
    nome_cartella = f"Fatture_{anno}"
    if not os.path.exists(nome_cartella):
        os.mkdir(nome_cartella)

# recupero informazioni su files e cartelle
print(os.path.getsize("sales.csv"))

print(os.path.getctime("sales.csv"))
"2/3/25"
