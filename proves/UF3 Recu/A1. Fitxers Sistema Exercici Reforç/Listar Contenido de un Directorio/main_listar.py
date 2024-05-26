from listar_contenido import listar_contenido

def main():
    directorio = input("Ingrese la ruta del directorio: ")
    contenido = listar_contenido(directorio)
    print("Contenido del directorio:")
    for item in contenido:
        print(item)

if __name__ == "__main__":
    main()
