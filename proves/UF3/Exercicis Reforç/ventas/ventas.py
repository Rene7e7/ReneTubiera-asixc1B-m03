import os

def registrar_venta(registro, producto, cantidad, precio):
    registro.append({"producto": producto, "cantidad": cantidad, "precio": precio})
    with open("registre_ventes.txt", "a") as f:
        f.write(f"Producte: {producto}, Quantitat: {cantidad}, Preu: {precio}\n")

def calcular_total(registro):
    return sum([venta["cantidad"] * venta["precio"] for venta in registro])

def guardar_registro(ruta_fitxer, registro):
    with open(ruta_fitxer, "w") as f:
        for venta in registro:
            f.write(f"Producte: {venta['producto']}, Quantitat: {venta['cantidad']}, Preu: {venta['precio']}\n")

def llegir_registro(ruta_fitxer):
    try:
        with open(ruta_fitxer, "r") as f:
            return [venta.strip().split(", ") for venta in f.readlines()]
    except FileNotFoundError:
        print("El fitxer no existeix.")
        return []

def crear_directoris():
    if not os.path.exists("registres"):
        os.makedirs("registres")

def guardar_registre(venta):
    with open(os.path.join("registres", f"venta_{len(os.listdir('registres')) + 1}.txt"), "w") as f:
        f.write(f"Producte: {venta['producto']}, Quantitat: {venta['cantidad']}, Preu: {venta['precio']}\n")
