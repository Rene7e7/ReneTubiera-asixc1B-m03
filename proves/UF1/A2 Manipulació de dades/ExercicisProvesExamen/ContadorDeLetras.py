"""
Rene Tubiera Sadinas
15/10/2023
UF1
Exercicis per l'examen
Solicita al usuario que ingrese una palabra y cuente cuántas letras contiene. Muestra el número de letras en la pantalla.

Estos ejercicios son similares en estructura a los anteriores, pero abordan diferentes aspectos, como cálculos matemáticos, verificaciones de edad, manipulación de cadenas y conversiones de unidades. Puedes intentar resolverlos y verificar tus respuestas.

"""
# Demana a l'usuari una paraula
palabra = input("Ingresa una palabra: ")
# Enumera los caracteres de la palabra i tambien remplaza los espacios i los elimina
num_letras = len(palabra.replace(" ",""))
print("La palabra tiene", num_letras, "letras.")

