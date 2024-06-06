# escribir_resultado.py
def escribir_resultado(ruta, contenido):
    with open(ruta, 'w', encoding='utf-8') as file:
        file.write(contenido)
