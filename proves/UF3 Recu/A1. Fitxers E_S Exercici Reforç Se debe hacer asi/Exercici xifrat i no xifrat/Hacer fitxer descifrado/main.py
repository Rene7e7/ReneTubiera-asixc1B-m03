import leer_archivo
import escribir_archivo
import descifrar

def main():
    # Nombre del archivo cifrado
    archivo_cifrado = 'texto_cifrado.txt'
    # Nombre del archivo descifrado
    archivo_descifrado = 'texto_descifrado.txt'
    # Clave de cifrado
    clave = 3  # Debe ser la misma clave que se usó para cifrar

    # Leer el archivo cifrado
    contenido_cifrado = leer_archivo.leer_archivo(archivo_cifrado)

    if contenido_cifrado is not None:
        # Descifrar el contenido
        contenido_descifrado = descifrar.descifrar(contenido_cifrado, clave)
        escribir_archivo.escribir_archivo(archivo_descifrado, contenido_descifrado)

    print("Proceso completado. El texto se ha descifrado y guardado correctamente.")

if __name__ == "__main__":
    main()
