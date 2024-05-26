def contar_digitos(texto):
    contador = 0
    for caracter in texto:
        if caracter.isdigit():
            contador += 1
    return contador
