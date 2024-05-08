def afegir_tasca(registre, tasca):
    registre.append({"tasca": tasca, "completada": False})

def marcar_completada(registre, index):
    if 0 <= index < len(registre):
        registre[index]["completada"] = True

def guardar_tasques(ruta_fitxer, registre):
    with open(ruta_fitxer, "w") as f:
        for tasca in registre:
            f.write(f"{tasca['tasca']},{tasca['completada']}\n")

def llegir_tasques(ruta_fitxer):
    try:
        with open(ruta_fitxer, "r") as f:
            registre = []
            for linia in f:
                tasca, completada = linia.strip().split(",")
                registre.append({"tasca": tasca, "completada": completada == "True"})
            return registre
    except FileNotFoundError:
        print("El fitxer no existeix.")
        return []
