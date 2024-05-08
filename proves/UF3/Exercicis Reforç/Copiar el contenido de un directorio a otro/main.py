import funciones

def main():
    origen = input("Introduce la ruta del directorio de origen: ")
    destino = input("Introduce la ruta del directorio de destino: ")
    funciones.copiar_directorio(origen, destino)

if __name__ == "__main__":
    main()
