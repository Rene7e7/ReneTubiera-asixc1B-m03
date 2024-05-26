import funciones_eliminar_lineas_vacias as felv

def main():
    ruta_archivo = input("Introduce la ruta del archivo de texto: ")
    felv.eliminar_lineas_vacias(ruta_archivo)
    print("Líneas vacías eliminadas correctamente.")

if __name__ == "__main__":
    main()
