def procesar_numeros(archivo_entrada, archivo_salida):
    try:
        with open(archivo_entrada, 'r', encoding='utf-8') as archivo:
            numeros = archivo.read().split()
            numeros = [float(num) for num in numeros]
            suma_total = sum(numeros)

        with open(archivo_salida, 'w', encoding='utf-8') as archivo:
            archivo.write(f'La suma total de los números es: {suma_total}\n')
    except FileNotFoundError:
        print(f"Error: El archivo '{archivo_entrada}' no se encontró.")
    except PermissionError:
        print(f"Error: No tienes permisos para escribir en '{archivo_salida}'.")
    except ValueError:
        print('El archivo contiene elementos que no son números.')
    except Exception as e:
        print(f"Error al procesar los archivos: {e}")

if __name__ == "__main__":
    procesar_numeros('numeros.txt', 'resultado_suma.txt')
