def main():
    archivo_entrada = 'notas.txt'
    archivo_salida = 'resultado_notas.txt'

    # Leer el contenido del archivo
    try:
        with open(archivo_entrada, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()
    except FileNotFoundError:
        print(f"Error: El archivo '{archivo_entrada}' no se encontró.")
        return
    except Exception as e:
        print(f"Error al leer el archivo '{archivo_entrada}': {e}")
        return

    if contenido is not None:
        # Extraer las notas y calcular el promedio
        notas = contenido.split()
        try:
            notas = [float(nota) for nota in notas]
            promedio = sum(notas) / len(notas) if notas else 0
        except ValueError:
            print('El archivo contiene elementos que no son números.')
            return

        # Escribir el resultado
        try:
            with open(archivo_salida, 'w', encoding='utf-8') as archivo:
                archivo.write(f'El promedio de las notas es: {promedio}\n')
        except PermissionError:
            print(f"Error: No tienes permisos para escribir en '{archivo_salida}'.")
        except Exception as e:
            print(f"Error al escribir en el archivo '{archivo_salida}': {e}")

if __name__ == "__main__":
    main()
