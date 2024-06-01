def intercambiar_mayusculas_minusculas(texto):
    try:
        # Intercambiar mayúsculas y minúsculas
        return texto.swapcase()
    except Exception as e:
        print(f"Error al intercambiar mayúsculas y minúsculas: {e}")
        return None
