# Built-in functions

numSenser = 65
caracter = "😀"

cadena = "Hola Mundo"

print(chr(numSenser))   # A

print(ord(caracter))    # 128512

print(len(cadena))      # 10

print("El caràcter "+caracter+" té el valor "+str(ord(caracter))) # El caràcter 😀 té el valor 128512

print(f"El caràcter {caracter} té el valor {str(ord(caracter))}")       # El caràcter 😀 té el valor 128512

print(f"El caràcter %s té el valor %d" % (caracter, ord(caracter)))     # El caràcter 😀 té el valor 128512

