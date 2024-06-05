def clasificar_alumnos(contenido):
    lineas = contenido.splitlines()
    clasificaciones = {
        'suspenso': [],
        'bien': [],
        'notable': [],
        'excelente': []
    }

    for linea in lineas:
        nombre, nota_str = linea.split(',')
        nota = float(nota_str.strip())

        # Mapeo de notas a categorías
        if nota < 5:
            clasificaciones['suspenso'].append((nombre, nota))
        elif 5 <= nota <= 6:
            clasificaciones['bien'].append((nombre, nota))
        elif 7 <= nota <= 8:
            clasificaciones['notable'].append((nombre, nota))
        elif 9 <= nota <= 10:
            clasificaciones['excelente'].append((nombre, nota))

    return clasificaciones

def escribir_resultados(archivo_salida, alumnos):
    try:
        with open(archivo_salida, 'w', encoding='utf-8') as archivo:
            for nombre, nota in alumnos:
                archivo.write(f'{nombre}, {nota}\n')
    except PermissionError:
        print(f"Error: No tienes permisos para escribir en '{archivo_salida}'.")
    except Exception as e:
        print(f"Error al escribir en el archivo '{archivo_salida}': {e}")

def leer_archivo(archivo_entrada):
    try:
        with open(archivo_entrada, 'r', encoding='utf-8') as archivo:
            return archivo.read()
    except FileNotFoundError:
        print(f"Error: El archivo '{archivo_entrada}' no se encontró.")
        return None
    except Exception as e:
        print(f"Error al leer el archivo '{archivo_entrada}': {e}")
        return None

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
