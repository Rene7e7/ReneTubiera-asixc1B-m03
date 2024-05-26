import funciones_sumar_numeros as fsn

def main():
    ruta_archivo = input("Introduce la ruta del archivo de texto: ")
    suma = fsn.sumar_numeros(ruta_archivo)
    print(f"La suma de los números en el archivo es: {suma}")

if __name__ == "__main__":
    main()
