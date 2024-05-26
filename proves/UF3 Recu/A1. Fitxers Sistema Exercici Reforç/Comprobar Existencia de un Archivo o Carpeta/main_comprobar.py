from comprobar_existencia import comprobar_existencia, obtener_rutas

def main():
    ruta = input("Ingrese la ruta del archivo o carpeta: ")
    existencia = comprobar_existencia(ruta)
    if existencia.startswith("El"):
        print(existencia)
        return
    else:
        ruta_absoluta, ruta_relativa = obtener_rutas(ruta)
        print(f"Ruta absoluta: {ruta_absoluta}")
        print(f"Ruta relativa: {ruta_relativa}")

if __name__ == "__main__":
    main()
