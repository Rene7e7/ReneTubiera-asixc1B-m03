def cifrar(texto, clave):
    resultado = []

    for char in texto:
        # Cifrado para letras mayúsculas
        if char.isupper():
            resultado.append(chr((ord(char) + clave - 65) % 26 + 65))
        # Cifrado para letras minúsculas
        elif char.islower():
            resultado.append(chr((ord(char) + clave - 97) % 26 + 97))
        else:
            # Otros caracteres no se cifran
            resultado.append(char)

    return ''.join(resultado)
