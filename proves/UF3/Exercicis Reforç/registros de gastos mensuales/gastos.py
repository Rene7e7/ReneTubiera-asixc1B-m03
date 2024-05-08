def afegir_gasto(registre, concepte, importe):
    registre.append({"concepte": concepte, "import": importe})

def total_gastos(registre):
    return sum(gasto["import"] for gasto in registre)

def guardar_gastos(ruta_fitxer, registre):
    with open(ruta_fitxer, "w") as f:
        for gasto in registre:
            f.write(f"{gasto['concepte']},{gasto['import']}\n")

def llegir_gastos(ruta_fitxer):
    try:
        with open(ruta_fitxer, "r") as f:
            registre = []
            for linia in f:
                concepte, importe = linia.strip().split(",")
                registre.append({"concepte": concepte, "import": float(importe)})
            return registre
    except FileNotFoundError:
        print("El fitxer no existeix.")
        return []
