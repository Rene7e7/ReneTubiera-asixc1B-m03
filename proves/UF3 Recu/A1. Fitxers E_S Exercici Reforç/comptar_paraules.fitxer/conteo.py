def comptar_paraules(frases):
    for i, frase in enumerate(frases):
        if frase.strip() == 'FI':
            break
        print(f'La línia {i+1} té {len(frase.split())} paraules.')
