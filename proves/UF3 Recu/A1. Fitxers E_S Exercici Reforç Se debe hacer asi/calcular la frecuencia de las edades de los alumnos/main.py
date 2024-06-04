import leer_archivo
import escribir_archivo
import calcular_frecuencia

def main():
    # Nombre del archivo de entrada
    archivo_entrada = 'edades_alumnos.txt'
    # Nombre del archivo de salida
    archivo_salida = 'frecuencia_edades.txt'

    # Leer las edades de los alumnos desde el archivo
    datos_alumnos = leer_archivo.leer_datos(archivo_entrada)

    if datos_alumnos is not None:
        # Extraer las edades de los datos de los alumnos
        edades = [int(datos.split(';')[1]) for datos in datos_alumnos]
        # Calcular la frecuencia de las edades
        frecuencia = calcular_frecuencia.calcular_frecuencia(edades)
        # Escribir la frecuencia de las edades en el archivo de salida
        escribir_archivo.escribir_frecuencia(archivo_salida, frecuencia)

    print("Proceso completado. La frecuencia de las edades se ha calculado y guardado correctamente.")

if __name__ == "__main__":
    main()
