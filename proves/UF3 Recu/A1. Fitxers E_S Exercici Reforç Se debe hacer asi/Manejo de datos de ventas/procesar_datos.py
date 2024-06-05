# procesar_datos.py

def calcular_total_ventas(datos):
    lineas = datos.split('\n')
    ventas = [float(linea.split(',')[1]) for linea in lineas[1:] if linea.strip()]
    return sum(ventas)

def calcular_promedio_ventas(datos):
    lineas = datos.split('\n')[1:]  # Saltar la primera línea
    ventas = [float(linea.split(',')[1]) for linea in lineas if linea.strip()]
    if ventas:
        return sum(ventas) / len(ventas)
    else:
        return 0
