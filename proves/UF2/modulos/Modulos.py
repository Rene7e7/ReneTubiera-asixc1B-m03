# Ejemplo 1: Importar un módulo completo
import math

# Utilizar la función sqrt() del módulo math para calcular la raíz cuadrada de un número
numero = 25
raiz_cuadrada = math.sqrt(numero)
print("Raíz cuadrada de", numero, "es:", raiz_cuadrada)

# Ejemplo 2: Importar funciones específicas de un módulo
from random import randint, choice

# Utilizar las funciones randint() y choice() del módulo random para generar números aleatorios y elegir elementos aleatorios de una lista
num_aleatorio = randint(1, 100)
print("Número aleatorio entre 1 y 100:", num_aleatorio)

lista = ['a', 'b', 'c', 'd', 'e']
elemento_aleatorio = choice(lista)
print("Elemento aleatorio de la lista:", elemento_aleatorio)

# Ejemplo 3: Renombrar un módulo al importarlo
import datetime as dt

# Utilizar las clases datetime y timedelta del módulo datetime para trabajar con fechas y tiempos
hoy = dt.datetime.today()
print("Fecha y hora actual:", hoy)

manana = hoy + dt.timedelta(days=1)
print("Mañana será:", manana)

# Ejemplo 4: Importar un módulo desde un paquete
from sklearn.linear_model import LinearRegression

# Utilizar la clase LinearRegression del módulo linear_model del paquete sklearn para crear un modelo de regresión lineal
modelo = LinearRegression()
print("Modelo de regresión lineal:", modelo)
# Importar el módulo colorama
import colorama

# Inicializar colorama para que los colores funcionen en la terminal
colorama.init()

# Ejemplo de impresión de texto en diferentes colores y estilos
print(colorama.Fore.RED + "Texto en rojo")
print(colorama.Fore.GREEN + "Texto en verde")
print(colorama.Fore.BLUE + "Texto en azul")

print(colorama.Style.BRIGHT + colorama.Fore.YELLOW + "Texto en amarillo brillante")
print(colorama.Style.RESET_ALL)  # Resetear los estilos de color

# Ejemplo de impresión de texto con colores de fondo
print(colorama.Back.RED + "Fondo rojo con texto normal")
print(colorama.Back.GREEN + colorama.Fore.WHITE + "Fondo verde con texto blanco")

# Resetear los colores de fondo y texto
print(colorama.Style.RESET_ALL)
