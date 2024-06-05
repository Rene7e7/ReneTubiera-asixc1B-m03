from leer_archivo import leer_archivo
from procesar_datos import obtener_usuarios_gmail
from escribir_resultado import escribir_resultado

def main(archivo_entrada, archivo_salida):
    correos = leer_archivo(archivo_entrada)
    if correos:
        usuarios_gmail = obtener_usuarios_gmail(correos)
        escribir_resultado(archivo_salida, usuarios_gmail)

if __name__ == "__main__":
    archivo_entrada = "correos.txt"
    archivo_salida = "usuarios_gmail.txt"
    main(archivo_entrada, archivo_salida)
