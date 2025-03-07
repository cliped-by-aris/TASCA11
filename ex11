import os

def llegir_fitxer(nom_fitxer):
    if not os.path.exists(nom_fitxer):
        print("Error: El fitxer no existeix.")
        return None
    
    try:
        with open(nom_fitxer, 'r', encoding='utf-8') as fitxer:
            return fitxer.read()
    except Exception as e:
        print(f"Error en llegir el fitxer: {e}")
        return None