def afegir_empleat(registre, nom, cognoms, departament):
    registre.append({"nom": nom, "cognoms": cognoms, "departament": departament})

def buscar_empleat(registre, nom):
    return [empleat for empleat in registre if empleat["nom"] == nom]

def guardar_empleats(ruta_fitxer, registre):
    with open(ruta_fitxer, "w") as f:
        for empleat in registre:
            f.write(f"{empleat['nom']},{empleat['cognoms']},{empleat['departament']}\n")

def llegir_empleats(ruta_fitxer):
    try:
        with open(ruta_fitxer, "r") as f:
            registre = []
            for linia in f:
                nom, cognoms, departament = linia.strip().split(",")
                registre.append({"nom": nom, "cognoms": cognoms, "departament": departament})
            return registre
    except FileNotFoundError:
        print("El fitxer no existeix.")
        return []
