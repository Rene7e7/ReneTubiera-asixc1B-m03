def escribir_resultados(archivo_salida, alumnos, estado):
    try:
        with open(archivo_salida, 'w', encoding='utf-8') as archivo:
            for nombre, nota in alumnos:
                archivo.write(f'{nombre}, {nota}, {estado}\n')
    except PermissionError:
        print(f"Error: No tienes permisos para escribir en '{archivo_salida}'.")
    except Exception as e:
        print(f"Error al escribir en el archivo '{archivo_salida}': {e}")

def leer_archivo(archivo_entrada):
    try:
        with open(archivo_entrada, 'r', encoding='utf-8') as archivo:
            return archivo.readlines()
    except FileNotFoundError:
        print(f"Error: El archivo '{archivo_entrada}' no se encontró.")
        return None
    except Exception as e:
        print(f"Error al leer el archivo '{archivo_entrada}': {e}")
        return None

def procesar_notas(lista_notas):
    aprobados = []
    suspendidos = []
    for linea in lista_notas:
        nombre, nota_str = linea.strip().split(', ')
        try:
            nota = float(nota_str)
            if 5 <= nota <= 10:
                aprobados.append((nombre, nota))
            elif 0 <= nota < 5:
                suspendidos.append((nombre, nota))
        except ValueError:
            print(f"Error: '{nota_str}' no es un número válido.")
    return aprobados, suspendidos

# Asegúrate de que las funciones estén definidas aquí o importadas correctamente
if __name__ == "__main__":
    lista_notas = leer_archivo('notas.txt')
    if lista_notas is not None:
        aprobados, suspendidos = procesar_notas(lista_notas)
        escribir_resultados('aprobados.txt', aprobados, 'Aprobado')
        escribir_resultados('suspendidos.txt', suspendidos, 'Suspendido')
