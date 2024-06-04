def descifrar(texto, clave):
    resultado = []

    for char in texto:
        # Descifrado para letras mayúsculas
        if char.isupper():
            resultado.append(chr((ord(char) - clave - 65) % 26 + 65))
        # Descifrado para letras minúsculas
        elif char.islower():
            resultado.append(chr((ord(char) - clave - 97) % 26 + 97))
        else:
            # Otros caracteres no se descifran
            resultado.append(char)

    return ''.join(resultado)
