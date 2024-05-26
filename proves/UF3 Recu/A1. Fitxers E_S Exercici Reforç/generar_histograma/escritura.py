def escribir_histograma(nombre_archivo, histograma):
    try:
        with open(nombre_archivo, 'w') as file:
            file.write("Histograma del archivo {}\n".format(nombre_archivo))
            file.write('-' * 30 + '\n')
            for categoria, cantidad in histograma.items():
                file.write(f"{categoria}: {cantidad}\n")
        print(f"El histograma se ha guardado correctamente en '{nombre_archivo}'.")
    except Exception as e:
        print(f"Error al escribir el histograma en '{nombre_archivo}': {e}")
