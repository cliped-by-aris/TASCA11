import random

def crear_taulell():
    return [[" " for _ in range(3)] for _ in range(3)]

def mostrar_taulell(taulell):
    for fila in taulell:
        print(" | ".join(fila))
        print("-" * 9)

def moviment_valid(taulell, fila, columna):
    return 0 <= fila < 3 and 0 <= columna < 3 and taulell[fila][columna] == " "

def fer_moviment(taulell, fila, columna, jugador):
    taulell[fila][columna] = jugador

def guanyador(taulell, jugador):
    for fila in taulell:
        if all(casella == jugador for casella in fila):
            return True
    for columna in range(3):
        if all(taulell[fila][columna] == jugador for fila in range(3)):
            return True
    if all(taulell[i][i] == jugador for i in range(3)) or all(taulell[i][2 - i] == jugador for i in range(3)):
        return True
    return False

def taulell_ple(taulell):
    return all(taulell[fila][columna] != " " for fila in range(3) for columna in range(3))

def moviment_maquina(taulell):
    moviments_disponibles = [(fila, columna) for fila in range(3) for columna in range(3) if taulell[fila][columna] == " "]
    return random.choice(moviments_disponibles)

def jugar():
    taulell = crear_taulell()
    mode = input("Mode de joc (1: contra màquina, 2: dos jugadors): ")
    jugador_actual = "X"
    while True:
        mostrar_taulell(taulell)
        if mode == "1" and jugador_actual == "O":
            fila, columna = moviment_maquina(taulell)
            print(f"La màquina mou a ({fila+1}, {columna+1})")
        else:
            fila, columna = map(int, input(f"Jugador {jugador_actual}, introdueix fila i columna (1-3): ").split())
            fila -= 1
            columna -= 1
            while not moviment_valid(taulell, fila, columna):
                print("Moviment invàlid. Torna a intentar-ho.")
                fila, columna = map(int, input(f"Jugador {jugador_actual}, introdueix fila i columna (1-3): ").split())
                fila -= 1
                columna -= 1
        fer_moviment(taulell, fila, columna, jugador_actual)
        if guanyador(taulell, jugador_actual):
            mostrar_taulell(taulell)
            print(f"El jugador {jugador_actual} ha guanyat!")
            break
        if taulell_ple(taulell):
            mostrar_taulell(taulell)
            print("Empat!")
            break
        jugador_actual = "O" if jugador_actual == "X" else "X"

jugar()