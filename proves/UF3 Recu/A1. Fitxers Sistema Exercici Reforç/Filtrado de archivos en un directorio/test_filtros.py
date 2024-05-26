from filtrar_por_extension import filtrar_por_extension
from filtrar_por_nombre import filtrar_por_nombre
from filtrar_ocultos import filtrar_ocultos

def test_filtros():
    # Pruebas para filtrar por extensión
    assert filtrar_por_extension(".", "txt") != []
    assert filtrar_por_extension(".", "py") != []

    # Pruebas para filtrar por nombre
    assert filtrar_por_nombre(".", "test") != []

    # Pruebas para filtrar archivos ocultos
    assert filtrar_ocultos(".", ocultos=True) != []
    assert filtrar_ocultos(".", ocultos=False) != []

if __name__ == "__main__":
    test_filtros()
    print("Todas las pruebas han pasado correctamente.")
