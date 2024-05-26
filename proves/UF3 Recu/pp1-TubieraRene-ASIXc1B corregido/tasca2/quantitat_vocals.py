def contar_vocales(palabra):
    cantidad_vocales = sum(1 for letra in palabra if letra.lower() in 'aeiou')
    return cantidad_vocales

def escribir_resultado(archivo_salida, palabra, cantidad_vocales):
    with open(archivo_salida, 'a') as archivo:
        archivo.write(f"{palabra}: {cantidad_vocales}\n")



