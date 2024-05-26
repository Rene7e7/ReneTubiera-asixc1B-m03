def concatenar_archivos(rutas_archivos, archivo_nuevo):
    with open(archivo_nuevo, "w") as f_destino:
        for ruta_archivo in rutas_archivos:
            try:
                with open(ruta_archivo, "r") as f_origen:
                    contenido = f_origen.read()
                    f_destino.write(contenido)
            except FileNotFoundError:
                print(f"El archivo {ruta_archivo} no existe.")
