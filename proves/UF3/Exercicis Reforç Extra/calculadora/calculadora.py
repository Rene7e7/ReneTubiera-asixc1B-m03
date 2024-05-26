def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacio(a, b):
    return a * b

def divisio(a, b):
    return a / b

def guardar_historial(ruta_fitxer, historial):
    with open(ruta_fitxer, "w") as f:
        for operacio in historial:
            f.write(f"{operacio}\n")

def llegir_historial(ruta_fitxer):
    try:
        with open(ruta_fitxer, "r") as f:
            historial = []
            for linia in f:
                historial.append(linia.strip())
            return historial
    except FileNotFoundError:
        print("El fitxer no existeix.")
        return []
