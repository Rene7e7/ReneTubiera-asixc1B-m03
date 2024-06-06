from leer_archivo import leer_archivo
from escribir_resultado import escribir_resultado
from actualizar_inventario import actualizar_inventario
from generar_informe import generar_informe

def gestionar_inventario(archivo_inventario, archivo_transacciones, archivo_informe):
    inventario = leer_archivo(archivo_inventario)
    transacciones = leer_archivo(archivo_transacciones)

    # Parsear la información del inventario y las transacciones
    inventario = dict([linea.split(',') for linea in inventario.strip().split('\n')])
    transacciones = [tuple(linea.split(',')) for linea in transacciones.strip().split('\n')]

    inventario_actualizado = actualizar_inventario(inventario, transacciones)
    informe = generar_informe(inventario_actualizado)
    escribir_resultado(archivo_informe, informe)

# Ejemplo de uso
if __name__ == "__main__":
    gestionar_inventario("inventario.txt", "transacciones.txt", "informe.txt")
