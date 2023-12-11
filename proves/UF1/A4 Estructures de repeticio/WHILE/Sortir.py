cont = 0  # Inicialización del contador
sortir = False  # Inicialización de la variable de control

# Bucle while que se ejecuta hasta que sortir sea True
while not sortir:
    cont = cont + 1  # Incrementa el contador en 1 en cada iteración
    print(cont)  # Imprime el valor actual del contador

    opcio = input("Sortir? (s/n): ")  # Solicita al usuario ingresar 's' o 'n' para salir o continuar
    if opcio.lower() == "s":  # Convierte la entrada del usuario a minúsculas y verifica si es "s"
        sortir = True  # Si es "s", cambia la variable de control a True para salir del bucle

# Se imprime un mensaje después de salir del bucle
print("Has sortit ... ets lliure ;-)")
