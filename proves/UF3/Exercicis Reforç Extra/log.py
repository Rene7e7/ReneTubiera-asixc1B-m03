import datetime

def escribir_log(mensaje):
    try:
        with open("log/log.txt", "a") as archivo_log:
            marca_tiempo = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            archivo_log.write(f"[{marca_tiempo}] {mensaje}\n")
    except FileNotFoundError:
        print("Error: No se encontró el archivo de registro.")
    except PermissionError:
        print("Error: Permiso denegado para escribir en el archivo de registro.")
    except Exception as e:
        print(f"Error inesperado al escribir en el archivo de registro: {e}")
