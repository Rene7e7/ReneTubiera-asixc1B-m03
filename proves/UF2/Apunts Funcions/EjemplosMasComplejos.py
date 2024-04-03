# Funciones matemáticas y numéricas
# Calcular el promedio de una lista de números
def calcular_promedio(nums):
    return sum(nums) / len(nums)

# Funciones de conversión de tipos
# Convertir una lista de números en una lista de cadenas de caracteres
def convertir_a_cadenas(nums):
    return [str(num) for num in nums]

# Funciones de cadenas de caracteres
# Contar el número de palabras en una oración
def contar_palabras(oracion):
    palabras = oracion.split()
    return len(palabras)

# Funciones de listas
# Encontrar el elemento más común en una lista
def elemento_mas_comun(lista):
    return max(set(lista), key=lista.count)

# Funciones de archivos y entrada/salida
# Leer un archivo y contar el número de líneas
def contar_lineas_archivo(ruta):
    try:
        with open(ruta, 'r') as archivo:
            lineas = archivo.readlines()
            return len(lineas)
    except FileNotFoundError:
        print("El archivo no se encontró.")
        return 0

# Funciones de control de flujo
# Comprobar si un número es primo
def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

# Funciones de manejo de errores
# Dividir dos números y manejar la excepción si se intenta dividir por cero
def division_segura(dividendo, divisor):
    try:
        resultado = dividendo / divisor
        return resultado
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")
        return None

# Funciones de tiempo
# Mostrar la hora actual en formato de 24 horas
import time

def hora_actual():
    hora_actual = time.strftime("%H:%M:%S")
    return hora_actual

# Ejemplo de uso de las funciones
numeros = [1, 2, 3, 4, 5]
print("Promedio:", calcular_promedio(numeros))

numeros_str = convertir_a_cadenas(numeros)
print("Lista convertida a cadenas:", numeros_str)

oracion = "Python es un lenguaje de programación poderoso"
print("Número de palabras:", contar_palabras(oracion))

lista = [1, 2, 3, 4, 2, 2, 5, 6, 7, 2]
print("Elemento más común:", elemento_mas_comun(lista))

ruta_archivo = "archivo.txt"
print("Número de líneas en el archivo:", contar_lineas_archivo(ruta_archivo))

numero = 17
if es_primo(numero):
    print(numero, "es primo")
else:
    print(numero, "no es primo")

dividendo = 10
divisor = 0
resultado = division_segura(dividendo, divisor)
if resultado is not None:
    print("Resultado de la división:", resultado)

print("Hora actual:", hora_actual())
