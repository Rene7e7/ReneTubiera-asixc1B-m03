def procesar_contenido(contenido):
    numeros = []

    for caracter in contenido:
        if caracter.isdigit():
            numeros.append(caracter)

    # Quiero que cada línea solo tenga 10 números
    resultado = ""
    for i in range(0, len(numeros), 10):
        resultado += " ".join(numeros[i:i+10]) + "\n"

    return resultado
