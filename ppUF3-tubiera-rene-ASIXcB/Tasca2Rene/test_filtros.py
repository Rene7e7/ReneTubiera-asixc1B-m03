from filtrar_por_extension import filtrar_por_extension

def test_filtros():
    # Lo que fa es detectar els fitxers que tenen extensio py en el directori actual
    assert filtrar_por_extension(".", "py") != []

if __name__ == "__main__":
    test_filtros()