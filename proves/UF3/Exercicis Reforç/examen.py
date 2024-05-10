def leer_archivo_y_filtrar(archivo_entrada, archivo_terminaciones, archivo_otras):
    # Abrir el archivo de entrada en modo lectura
    with open(archivo_entrada, 'r') as archivo:
        # Leer todas las líneas del archivo
        lineas = archivo.readlines()

    # Abrir los archivos de salida en modo escritura
    with open(archivo_terminaciones, 'w') as archivo_terminaciones, \
         open(archivo_otras, 'w') as archivo_otras:
        # Iterar sobre cada línea del archivo
        for linea in lineas:
            # Dividir la línea en palabras
            palabras = linea.split()
            # Iterar sobre cada palabra
            for palabra in palabras:
                # Si la palabra termina en 'cion', escribirla en archivo_terminaciones
                if palabra.endswith('cion'):
                    archivo_terminaciones.write(palabra + '\n')
                # Si no, escribirla en archivo_otras
                else:
                    archivo_otras.write(palabra + '\n')

# Nombre del archivo de entrada
archivo_entrada = 'texto.txt'
# Nombre del archivo para palabras que terminan en 'cion'
archivo_terminaciones = 'terminaciones.txt'
# Nombre del archivo para otras palabras
archivo_otras = 'otras.txt'

# Llamar a la función para leer el archivo de entrada y filtrar las palabras
leer_archivo_y_filtrar(archivo_entrada, archivo_terminaciones, archivo_otras)

print("Proceso completado. Las palabras se han filtrado y guardado correctamente.")

import ejercicio

def main():
    # Nombre del archivo de entrada
    archivo_entrada = 'texto.txt'
    # Nombre del archivo para palabras que terminan en 'cion'
    archivo_terminaciones = 'terminaciones.txt'
    # Nombre del archivo para otras palabras
    archivo_otras = 'otras.txt'

    # Llamar a la función para procesar el archivo
    ejercicio.procesar_archivo(archivo_entrada, archivo_terminaciones, archivo_otras)

    print("Proceso completado. Las palabras se han filtrado y guardado correctamente.")

if __name__ == "__main__":
    main()

def leer_archivo(archivo_entrada):
    with open(archivo_entrada, 'r') as archivo:
        return archivo.readlines()

def filtrar_palabras(lineas):
    palabras_terminacion = []
    otras_palabras = []

    for linea in lineas:
        palabras = linea.split()
        for palabra in palabras:
            if palabra.endswith('cion'):
                palabras_terminacion.append(palabra)
            else:
                otras_palabras.append(palabra)

    return palabras_terminacion, otras_palabras

def escribir_archivo(archivo_salida, palabras):
    with open(archivo_salida, 'w') as archivo:
        for palabra in palabras:
            archivo.write(palabra + '\n')

def procesar_archivo(archivo_entrada, archivo_terminaciones, archivo_otras):
    lineas = leer_archivo(archivo_entrada)
    palabras_terminacion, otras_palabras = filtrar_palabras(lineas)
    escribir_archivo(archivo_terminaciones, palabras_terminacion)
    escribir_archivo(archivo_otras, otras_palabras)
