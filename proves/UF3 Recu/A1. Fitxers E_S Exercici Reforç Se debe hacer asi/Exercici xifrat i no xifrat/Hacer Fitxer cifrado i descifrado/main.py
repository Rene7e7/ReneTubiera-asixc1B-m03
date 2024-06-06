import leer_archivo
import escribir_archivo
import cifrar
import descifrar

def main():
    # Nombre del archivo de entrada
    archivo_entrada = 'texto.txt'
    # Nombre del archivo cifrado
    archivo_cifrado = 'texto_cifrado.txt'
    # Nombre del archivo descifrado
    archivo_descifrado = 'texto_descifrado.txt'
    # Clave de cifrado
    clave = 3  # Puedes cambiar esta clave según tus necesidades

    # Leer el archivo de entrada
    contenido = leer_archivo.leer_archivo(archivo_entrada)

    if contenido is not None:
        # Cifrar el contenido
        contenido_cifrado = cifrar.cifrar(contenido, clave)
        escribir_archivo.escribir_archivo(archivo_cifrado, contenido_cifrado)

        # Leer el archivo cifrado
        contenido_cifrado_leido = leer_archivo.leer_archivo(archivo_cifrado)

        if contenido_cifrado_leido is not None:
            # Descifrar el contenido
            contenido_descifrado = descifrar.descifrar(contenido_cifrado_leido, clave)
            escribir_archivo.escribir_archivo(archivo_descifrado, contenido_descifrado)

    print("Proceso completado. El texto se ha cifrado y descifrado correctamente.")

if __name__ == "__main__":
    main()
