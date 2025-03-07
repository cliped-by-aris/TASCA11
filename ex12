import os

def crear_fitxer():
    directori = "/home/cicles/AO/Prova"
    fitxer_nom = os.path.join(directori, "Ex12.txt")

    os.makedirs(directori, exist_ok=True)

    with open(fitxer_nom, "w", encoding="utf-8") as f:
        f.write("Marc, Jordi, Juan Pablo, Aris, Ivan, David, Jaume, Eneko...\n")

    with open(fitxer_nom, "a", encoding="utf-8") as f:
        f.write("Pepe, Pep, Joan, Clara, Olga, Carlos, David\n")

    with open(fitxer_nom, "r", encoding="utf-8") as f:
        print(f.read())

crear_fitxer()