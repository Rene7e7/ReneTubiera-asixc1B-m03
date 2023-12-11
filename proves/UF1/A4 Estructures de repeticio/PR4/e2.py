"""
Jordi Yu y Rene Tubiera
M03 A4 Pr4
29/11/2023
Programa que mostra un triangle amb nombres a les cantonades.
Cal demanar quina alçada ha de tenir el triangle.
Els valors permesos per a l'alçada son entre 2 i 9. (ambdós inclosos)
"""
try:
    Suma = 0
    Num = int(input("Altura? "))

    # Verifica si la altura está dentro del rango permitido
    if Num > 9 or Num < 2:
        print("La altura debe estar entre 2 y 9")
    else:
        # Bucle externo para la altura del triángulo
        for i in range(1, Num+1):
            # Bucle interno para cada línea del triángulo
            for j in range(1, i + 1):
                # Verifica si es el primer, último elemento o la última línea
                if j == 1 or j == i or i == Num:
                    print(i, end=" ")
                    Suma += i
                # Si no es el primer o último elemento, imprime un espacio
                else:
                    print(" ", end=" ")
            # Imprime una nueva línea después de cada fila
            print()

except ValueError:
    # Captura el error si la entrada no es un número entero
    print("Error: Debes ingresar un número entero.")
except:
    # Captura cualquier otro tipo de error
    print("Error")
