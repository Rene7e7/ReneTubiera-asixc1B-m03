# Funciones matemáticas y numéricas
# abs(): Devuelve el valor absoluto de un número.
abs_num = abs(-10)
print(abs_num)  # Salida: 10

# round(): Redondea un número al entero más cercano.
rounded_num = round(3.75)
print(rounded_num)  # Salida: 4

# max(): Devuelve el valor máximo de una secuencia.
max_num = max(2, 5, 1, 8)
print(max_num)  # Salida: 8

# min(): Devuelve el valor mínimo de una secuencia.
min_num = min(2, 5, 1, 8)
print(min_num)  # Salida: 1

# sum(): Suma todos los elementos de una secuencia.
sum_nums = sum([2, 5, 1, 8])
print(sum_nums)  # Salida: 16

# pow(): Eleva un número a una potencia.
result = pow(2, 3)
print(result)  # Salida: 8

# divmod(): Devuelve el cociente y el residuo de la división entre dos números.
divmod_result = divmod(10, 3)
print(divmod_result)  # Salida: (3, 1)

# Funciones de conversión de tipos
# int(): Convierte un valor a entero.
int_num = int("10")
print(int_num)  # Salida: 10

# float(): Convierte un valor a flotante.
float_num = float("3.14")
print(float_num)  # Salida: 3.14

# str(): Convierte un valor a cadena de caracteres.
str_num = str(10)
print(str_num)  # Salida: '10'

# bool(): Convierte un valor a booleano.
bool_val = bool(0)
print(bool_val)  # Salida: False

# Funciones de cadenas de caracteres
# len(): Devuelve la longitud de una cadena de caracteres o una secuencia.
length = len("Hola Mundo")
print(length)  # Salida: 10

# upper(): Convierte una cadena de caracteres a mayúsculas.
upper_text = "Hola Mundo".upper()
print(upper_text)  # Salida: 'HOLA MUNDO'

# lower(): Convierte una cadena de caracteres a minúsculas.
lower_text = "Hola Mundo".lower()
print(lower_text)  # Salida: 'hola mundo'

# capitalize(): Convierte la primera letra de una cadena a mayúscula.
capitalized_text = "hola mundo".capitalize()
print(capitalized_text)  # Salida: 'Hola mundo'

# count(): Cuenta el número de ocurrencias de un subconjunto en una cadena.
count_o = "Hola Mundo".count("o")
print(count_o)  # Salida: 2

# find(): Encuentra la primera ocurrencia de un subconjunto en una cadena.
position = "Hola Mundo".find("Mundo")
print(position)  # Salida: 5

# split(): Divide una cadena en subcadenas utilizando un delimitador.
words = "Hola Mundo".split(" ")
print(words)  # Salida: ['Hola', 'Mundo']

# join(): Une una lista de cadenas en una sola cadena utilizando un delimitador.
text = " ".join(['Hola', 'Mundo'])
print(text)  # Salida: 'Hola Mundo'
