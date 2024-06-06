from leer_archivo_T1 import leer_archivo
from filtrar_palabras_longitud import filtrar_palabras_longitud
from escribir_palabras_T1 import escribir_palabras

def main():
    # Aquest es el arxiu de entrada que tindra que llegir el fitxer
    archivo_entrada = 'paraules.txt'
    # Aquest es el arxiu de sortida on escriura el resultat
    archivo_salida = 'paraules-mida.txt'
    # La variable longitud es la longitud de la paraula que es vol posar en el arxiu de sortida
    longitud = 15

    # Lo que fa es llegir el arxiu de entrada
    palabras = leer_archivo(archivo_entrada)
    # si el fitxer de entrada no existex no podra executar el programa
    if not palabras:
        print("No se puede procesar el archivo.")
        return

    # Identifica les paraules que tenen una mida de 15 caracters
    palabras_filtradas = filtrar_palabras_longitud(palabras, longitud)
    # Escriura en l'arxiu de sortida les paraules que tenen una mida de 15
    escribir_palabras(archivo_salida, palabras_filtradas)
    # mostra el missatge que s'ha executat corefctament
    print("Proceso completado. Las palabras con la longitud especificada se han guardado correctamente.")

# Executa el programa
if __name__ == "__main__":
    main()