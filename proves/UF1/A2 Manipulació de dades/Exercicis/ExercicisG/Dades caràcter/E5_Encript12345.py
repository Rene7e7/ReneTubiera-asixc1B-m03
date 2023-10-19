"""
11/10/2023
René Tubiera y Jordi Yu

E5. Encript12345
Demana una paraula per teclat i mostrar-la per pantalla, canviar les vocals per als numèrics 1, 2, 3, 4 o 5.
Tenint en compte, que la lletra a i A és l'1, consecutivament fins a la lletra u i U que és el 5.
"""

# Pedimos que escriba una palabra a l'usuario
palabra = input("Dime una palabra: ")

# Remplazamos los vocales (incluso las mayusculas) por numeros
palabra = palabra.replace('a', '1')
palabra = palabra.replace('A', '1')
palabra = palabra.replace('e', '2')
palabra = palabra.replace('E', '2')
palabra = palabra.replace('i', '2')
palabra = palabra.replace('I', '3')
palabra = palabra.replace('o', '3')
palabra = palabra.replace('O', '4')
palabra = palabra.replace('u', '4')
palabra = palabra.replace('U', '5')
palabra = palabra.replace('a', '5')

# Es mostrara la palabra modificada
print("La paraula ha sido modificado a ", palabra)