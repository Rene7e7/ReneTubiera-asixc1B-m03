PWD = "asdasd"
PIN = 1234
MAX_INTENTS = 3
intents = MAX_INTENTS
EASTER_EGG =""


clave = input("Dime la clave:")

# 3 intents
while clave != PIN and intents != 3 and clave != EASTER_EGG:
    print("Clave incorrecta!!!")
    intents = intents - 1
if clave == EASTER_EGG:
   print("Bienvenido!!!")
print("Programa terminado")
