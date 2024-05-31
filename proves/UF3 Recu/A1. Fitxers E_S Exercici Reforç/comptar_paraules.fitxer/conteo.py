def comptar_paraules(frases):
    # la funció enumerate() retorna una tupla amb un comptador i un element de la llista
    # linia per linia anem comptant les paraules
    # frase lo que fa és recórrer la llista frases
    # i és el comptador
    for i, frase in enumerate(frases):
        # strip lo que fa es eliminar els espais en blanc al principi i al final de la cadena
        if frase.strip() == 'FI':
            break
        # i + 1 perquè la primera línia és la 1 i no la 0
        print(f'La línia {i+1} té {len(frase.split())} paraules.')
