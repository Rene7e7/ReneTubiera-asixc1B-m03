def afegir_producte(registre, producte):
    registre.append({"producte": producte, "comprat": False})

def marcar_comprat(registre, index):
    if 0 <= index < len(registre):
        registre[index]["comprat"] = True

def guardar_compres(ruta_fitxer, registre):
    with open(ruta_fitxer, "w") as f:
        for compra in registre:
            f.write(f"{compra['producte']},{compra['comprat']}\n")

def llegir_compres(ruta_fitxer):
    try:
        with open(ruta_fitxer, "r") as f:
            registre = []
            for linia in f:
                producte, comprat = linia.strip().split(",")
                registre.append({"producte": producte, "comprat": comprat == "True"})
            return registre
    except FileNotFoundError:
        print("El fitxer no existeix.")
        return []
