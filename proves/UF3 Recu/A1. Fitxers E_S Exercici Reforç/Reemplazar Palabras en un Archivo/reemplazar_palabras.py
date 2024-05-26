def reemplazar_palabras(texto, palabra_a_reemplazar, palabra_de_reemplazo):
    try:
        texto_modificado = texto.replace(palabra_a_reemplazar, palabra_de_reemplazo)
        return texto_modificado
    except Exception as e:
        print(f"Error al reemplazar palabras: {e}")
        return None
