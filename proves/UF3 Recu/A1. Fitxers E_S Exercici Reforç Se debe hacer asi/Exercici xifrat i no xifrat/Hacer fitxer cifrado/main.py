import leer_archivo
import escribir_archivo
import cifrar

def main():
    # Nombre del archivo de entrada
    archivo_entrada = 'texto.txt'
    # Nombre del archivo cifrado
    archivo_cifrado = 'texto_cifrado.txt'
    # Clave de cifrado
    clave = 3  # Puedes cambiar esta clave según tus necesidades

    # Leer el archivo de entrada
    contenido = leer_archivo.leer_archivo(archivo_entrada)

    if contenido is not None:
        # Cifrar el contenido
        contenido_cifrado = cifrar.cifrar(contenido, clave)
        escribir_archivo.escribir_archivo(archivo_cifrado, contenido_cifrado)

    print("Proceso completado. El texto se ha cifrado y guardado correctamente.")

if __name__ == "__main__":
    main()
