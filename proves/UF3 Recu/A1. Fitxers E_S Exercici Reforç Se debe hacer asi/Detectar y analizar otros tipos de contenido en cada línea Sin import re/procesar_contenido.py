def procesar_contenido(contenido):
    resultados = []

    lineas = contenido.splitlines()
    vocales_set = set('AEIOUaeiouÀ-ÖØ-öø-ÿ')
    consonantes_set = set('BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz')

    for indice, linea in enumerate(lineas, start=1):
        palabras = 0
        numeros = 0
        caracteres_especiales = 0
        vocales = 0
        consonantes = 0
        es_palabra = False

        for caracter in linea:
            if caracter.isalpha():
                if not es_palabra:
                    palabras += 1
                    es_palabra = True
                if caracter in vocales_set:
                    vocales += 1
                elif caracter in consonantes_set:
                    consonantes += 1
            else:
                es_palabra = False
                if caracter.isdigit():
                    numeros += 1
                elif not caracter.isspace():
                    caracteres_especiales += 1

        resultados.append(
            f"Línea {indice}: {palabras} palabras, {numeros} números, {caracteres_especiales} caracteres especiales, "
            f"{vocales} vocales, {consonantes} consonantes"
        )

    return "\n".join(resultados)
