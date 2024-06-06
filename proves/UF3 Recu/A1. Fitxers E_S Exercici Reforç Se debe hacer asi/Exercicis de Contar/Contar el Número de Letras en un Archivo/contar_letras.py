def contar_letras(texto):
    # Inicializamos el contador a 0
    contador = 0
    # Recorremos el texto caracter a caracter
    for caracter in texto:
        # si el caracter es una letra
        if caracter.isalpha():
            # incrementamos el contador
            contador += 1
    # retornamos el contador
    return contador
