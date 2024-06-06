def escribir_palabras(archivo_salida, palabras, resultado):
    try:
        with open(archivo_salida, 'w', encoding='utf8') as archivo:
            # Itera paraula per paraula
            for palabra in palabras:
                # escriu les paraules amb un salt de linea per cada paraula
                archivo.write(palabra + '\n')
            # Dividim el text per paraules
            palabras = palabra.split()
            # Retorna el numero de paraules
            archivo.write(f"El archivo contiene {resultado} palabras.")


    except Exception as e:
        print(f"Error al escibrir en el archivo '{archivo_salida}': {e}")