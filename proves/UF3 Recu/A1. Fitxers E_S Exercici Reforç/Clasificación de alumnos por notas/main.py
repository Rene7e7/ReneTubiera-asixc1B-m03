from leer_archivo import leer_archivo
from clasificar_alumnos import clasificar_alumnos
from escribir_resultados import escribir_resultados

def main():
    archivo_entrada = 'notas_alumnos.txt'

    # Leer el contenido del archivo
    contenido = leer_archivo(archivo_entrada)

    if contenido is not None:
        # Clasificar a los alumnos por sus notas
        clasificaciones = clasificar_alumnos(contenido)

        # Escribir los resultados en los archivos correspondientes
        for categoria, alumnos in clasificaciones.items():
            escribir_resultados(f'{categoria}.txt', alumnos)

if __name__ == "__main__":
    main()
