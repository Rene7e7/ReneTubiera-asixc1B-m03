def afegir_estudiant(registre, nom, edat):
    registre.append({"nom": nom, "edat": edat})

def buscar_estudiant(registre, nom):
    for estudiant in registre:
        if estudiant["nom"] == nom:
            return estudiant
    return None

def guardar_registre(ruta_fitxer, registre):
    with open(ruta_fitxer, "w") as f:
        for estudiant in registre:
            f.write(f"{estudiant['nom']},{estudiant['edat']}\n")

def llegir_registre(ruta_fitxer):
    try:
        with open(ruta_fitxer, "r") as f:
            registre = []
            for linia in f:
                nom, edat = linia.strip().split(",")
                registre.append({"nom": nom, "edat": int(edat)})
            return registre
    except FileNotFoundError:
        print("El fitxer no existeix.")
        return []
