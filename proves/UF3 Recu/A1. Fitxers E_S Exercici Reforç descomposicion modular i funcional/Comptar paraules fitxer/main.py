def comptar_paraules(frases):
    for i, frase in enumerate(frases, start=1):
        if frase.strip().upper() == 'FI':
            break
        num_palabras = len(frase.split())
        print(f'La línea {i} tiene {num_palabras} palabra(s).')

def llegir_arxiu(ruta):
    try:
        with open(ruta, "r", encoding='utf-8') as f:
            return f.readlines()
    except FileNotFoundError:
        print(f"Error: El archivo '{ruta}' no se encontró.")
        return []
    except Exception as e:
        print(f"Error al leer el archivo '{ruta}': {e}")
        return []

def main():
    ruta = 'frases.txt'
    frases = llegir_arxiu(ruta)
    comptar_paraules(frases)

if __name__ == "__main__":
    main()
