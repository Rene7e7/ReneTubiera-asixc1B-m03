# Módulos de procesamiento de datos
from lectura import leer_notas
from procesamiento import generar_histograma
from escritura import escribir_histograma

def escribir_histograma(nombre_archivo, histograma):
    try:
        with open(nombre_archivo, 'w') as file:
            file.write(f"Histograma del archivo {nombre_archivo}\n")
            file.write('-' * 30 + '\n')
            for categoria, cantidad in histograma.items():
                file.write(f"{categoria}: {cantidad}\n")
        print(f"El histograma se ha guardado correctamente en '{nombre_archivo}'.")
    except IOError as e:
        print(f"Error al escribir el histograma en '{nombre_archivo}': {e}")

def leer_notas(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no se encontró.")
        return None
    except IOError as e:
        print(f"Error al leer el archivo '{nombre_archivo}': {e}")
        return None

def generar_histograma(contenido):
    if contenido is None:
        return None

    notas = contenido.split()
    histograma = {'Excel·lent': 0, 'Notable': 0, 'Aprovat': 0, 'Suspès': 0}
    for nota_str in notas:
        try:
            nota = float(nota_str.replace(',', '.'))
            if nota == -1:
                break
            if 9 <= nota <= 10:
                histograma['Excel·lent'] += 1
            elif 6.5 <= nota < 9:
                histograma['Notable'] += 1
            elif 5 <= nota < 6.5:
                histograma['Aprovat'] += 1
            elif nota < 5:
                histograma['Suspès'] += 1
        except ValueError:
            print(f"Advertencia: La nota '{nota_str}' no es un valor numérico válido. Se ignorará.")

    return histograma

def main():
    nombre_archivo = input("Introduce el nombre del archivo de notas: ")
    contenido = leer_notas(nombre_archivo)
    histograma = generar_histograma(contenido)

    if histograma:
        nombre_archivo_histograma = f"{nombre_archivo.split('.')[0]}-Histograma.txt"
        escribir_histograma(nombre_archivo_histograma, histograma)
    else:
        print("No se generó el histograma debido a un error en la lectura del archivo.")

if __name__ == "__main__":
    main()
