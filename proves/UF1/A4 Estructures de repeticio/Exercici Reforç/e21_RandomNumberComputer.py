import random

try:
    # Inicializar variables
    contador = 0  # Contador de intentos
    numero_secreto = int(input("Piensa en un número del 1 al 100: "))  # Número que el usuario debe adivinar
    limite_intentos = 10  # Número máximo de intentos permitidos
    adivinado = False  # Variable para indicar si la computadora ha adivinado el número

    # Bucle principal
    while contador < limite_intentos and not adivinado:
        # Generar un número aleatorio propuesto por la computadora
        num_computadora = random.randint(1, 100)
        print(f"La computadora propone: {num_computadora}")

        # Comprobar si la computadora ha adivinado correctamente
        if num_computadora == numero_secreto:
            print(f"¡La computadora ha adivinado tu número ({numero_secreto}) en el intento {contador + 1}!")
            adivinado = True  # Establecer la variable adivinado a True para salir del bucle
        else:
            # Solicitar al usuario información sobre si el número es mayor, menor o igual
            respuesta_usuario = input("El número es mayor, menor o igual al que has pensado? (M/m/I): ").lower()

            # Procesar la respuesta del usuario
            if respuesta_usuario == 'm':
                print("El número es más grande.")
            elif respuesta_usuario == 'i':
                print("¡La computadora ha adivinado tu número!")
                adivinado = True  # Establecer la variable adivinado a True para salir del bucle
            else:
                print("El número es más pequeño.")

        contador += 1  # Incrementar el contador de intentos

    # Imprimir mensaje final si la computadora no ha adivinado el número
    if not adivinado:
        print(f"La computadora no ha podido adivinar tu número en {limite_intentos} intentos. ¡Inténtalo tú mismo!")

except ValueError:
    print("Debe ingresar un número entero.")
