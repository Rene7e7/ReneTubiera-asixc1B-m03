data = str(input("Por favor, escribe una oración: "))  # Solicita al usuario que ingrese una oración y la guarda en la variable 'data'
vowels = "aeiou"  # Cadena que contiene las vocales
for v in vowels:  # Bucle que recorre cada vocal en la cadena 'vowels'
    print(v, data.lower().count(v))  # Imprime la vocal actual y la cuenta de esa vocal en la oración (ignorando mayúsculas/minúsculas)
