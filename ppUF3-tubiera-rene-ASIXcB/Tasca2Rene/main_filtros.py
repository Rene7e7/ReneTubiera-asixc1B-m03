from filtrar_archivos import filtrar_archivos
from comprobar_existencia import comprobar_existencia, obtener_rutas

def main():
    # Ens demana que posem una ruta de un directori
    directorio = input("Directorio: ")
    # La variable existencia lo que fa es comprobar la exsitencia de la ruta del directori que s'ha posat per teclat
    existencia = comprobar_existencia(directorio)
    # mostra els noms dels fitxers que tenen com a extensio py d'un directori
    extension = "py"
    # si els fitxers acaben en extensio py retorna
    if existencia.endswith("py"):
        return

    # mostar les ruta absoluta i relativa de la ruta que s'ha posat per teclat
    ruta_absoluta, ruta_relativa = obtener_rutas(directorio)
    print(f"Ruta absoluta: {ruta_absoluta}")
    print(f"Ruta relativa: {ruta_relativa}")

    # Filtra els arxius del directori amb la extensio especificat que es py
    archivos_filtrados = filtrar_archivos(directorio, extension)
    print("Archivos filtrados:")
    # itera arxiu per arxiu en els arxius filtrats
    for archivo in archivos_filtrados:
        print(archivo)

# executa el programa
if __name__ == "__main__":
    main()