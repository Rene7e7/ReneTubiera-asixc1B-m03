'''
Modificar l'exemple Recorregut de directoris recursiu, per a controlat els possibles errors.

Anotar en un fitxer *.log, els errors trobats (només) amb la data i hora del sistema.

'''
import datetime
import os

def recorrer_arbol_directorios(directorio):
    try:
        # Obtener la lista de archivos y directorios en el directorio actual
        contenido = os.listdir(directorio)
        # Recorrer cada elemento del directorio actual
        for elemento in contenido:
            # Crear la ruta completa del elemento
            ruta_elemento = os.path.join(directorio, elemento)
            # Si el elemento es un directorio, recorrer recursivamente
            if os.path.isdir(ruta_elemento):
                print("Directorio:", ruta_elemento)
                recorrer_arbol_directorios(ruta_elemento)
            else:
                print("Archivo:", ruta_elemento)
    except Exception as e:
        log_error(str(e))

def log_error(error):
    fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("log_error.log", mode='at', encoding='utf-8') as file:
        file.write(f"{fecha_hora} - {error}\n")
    print(f"Error: {error}")
    return error
# Función principal
def main():
    # Solicitar al usuario el directorio inicial
    directorio_inicial = input("Introduce la ruta del directorio inicial: ")
    # Verificar si el directorio ingresado existe
    if not os.path.isdir(directorio_inicial):
        print("El directorio especificado no existe.")
    else:
        # Llamar a la función recursiva para recorrer el árbol de directorios
        print("\nRecorrido del árbol de directorios:")
        recorrer_arbol_directorios(directorio_inicial)

if __name__ == "__main__":
    main()
    log_error("Error de prueba")
