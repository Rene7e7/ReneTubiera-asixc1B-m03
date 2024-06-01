def generar_histograma(contenido):
    if contenido is None:
        return None

    notas = contenido.split()
    histograma = {'Excel·lent': 0, 'Notable': 0, 'Aprovat': 0, 'Suspès': 0}
    # Iterar sobre las notas y contar cuántas hay de cada tipo
    for nota_str in notas:
        try:
            # Reemplazar la coma por un punto para que Python pueda convertir la cadena a un número decimal
            nota = float(nota_str.replace(',', '.'))
            if nota == -1:
                break
            if 9 <= nota <= 10:
                histograma['Excel·lent'] += 1
            elif 6.5 <= nota < 9:
                histograma['Notable'] += 1
            elif 5 <= nota < 6.5:
                histograma['Aprovat'] += 1
            elif nota < 5:
                histograma['Suspès'] += 1
        except ValueError:
            print(f"Advertencia: La nota '{nota_str}' no es un valor numérico válido. Se ignorará.")

    return histograma
