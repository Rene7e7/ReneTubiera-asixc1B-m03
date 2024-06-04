import leer_archivo
import escribir_archivo
import clasificar_alumnos

def main():
    # Nombre del archivo de entrada
    archivo_entrada = 'edades_alumnos.txt'
    # Nombre del archivo de salida para los alumnos mayores de edad
    archivo_mayores = 'alumnos_mayores.txt'
    # Nombre del archivo de salida para los alumnos menores de edad
    archivo_menores = 'alumnos_menores.txt'

    # Leer los datos de los alumnos desde el archivo
    datos_alumnos = leer_archivo.leer_datos(archivo_entrada)

    if datos_alumnos is not None:
        # Clasificar a los alumnos como mayores o menores de edad
        mayores_de_edad, menores_de_edad = clasificar_alumnos.clasificar_alumnos(datos_alumnos)

        # Escribir la clasificación de los alumnos mayores de edad en el archivo de salida
        escribir_archivo.escribir_clasificacion(archivo_mayores, mayores_de_edad)

        # Escribir la clasificación de los alumnos menores de edad en el archivo de salida
        escribir_archivo.escribir_clasificacion(archivo_menores, menores_de_edad)

    print("Proceso completado. La clasificación de los alumnos se ha guardado correctamente.")

if __name__ == "__main__":
    main()
