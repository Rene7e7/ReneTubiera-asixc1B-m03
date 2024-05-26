import paraules_caracters as pc

def main():
    archivo_entrada = "paraules.txt"  # Nombre del archivo de entrada
    longitudes_palabras = [2, 4, 6, 8, 10]  # Longitudes de palabras a buscar

    for longitud_palabra in longitudes_palabras:
        palabras_contador = pc.palabras(archivo_entrada, longitud_palabra)
        print(f"Se han encontrado {len(palabras_contador)} palabras de longitud {longitud_palabra}.")

if __name__ == "__main__":
    main()
