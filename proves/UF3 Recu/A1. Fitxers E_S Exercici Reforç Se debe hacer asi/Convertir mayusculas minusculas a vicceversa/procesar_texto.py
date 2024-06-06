# procesar_texto.py
def procesar_texto(texto):
    resultado = []
    for char in texto:
        if char.islower():
            resultado.append(char.upper())
        elif char.isupper():
            resultado.append(char.lower())
        else:
            resultado.append(char)
    return ''.join(resultado)
