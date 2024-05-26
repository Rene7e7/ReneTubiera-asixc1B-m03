from operaciones_directorio import crear_directorio, eliminar_directorio, renombrar_directorio, cambiar_permisos

def main():
    # Ejemplo de uso
    directorio = input("Ingrese el nombre del directorio: ")
    print(crear_directorio(directorio))
    print(eliminar_directorio(directorio))
    # Otros casos de prueba para las demás funciones

if __name__ == "__main__":
    main()
