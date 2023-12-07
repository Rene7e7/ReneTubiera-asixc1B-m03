"""
Jordi Yu y Rene Tubiera
M03 A4 Pr4
29/11/2023
Programa que mostra un triangle amb nombres a les cantonades.
Cal demanar quina alçada ha de tenir el triangle.
Els valors permesos per a l'alçada son entre 2 i 9. (ambdós inclosos)
"""
# Try y except para errores
try:
    Suma = 0
    Num = int(input("Altura? "))
# Los for para aumento del triangulo
    if Num>9 or Num<2:
        print("La altura debe ser entre 2 y 9")
    else:
        for i in range(1, Num+1):
            for j in range(1, i + 1):
# Este if para solucionar el problema del ultimo numero que no tiene vacio
                if j == 1 or j == i or i == Num:
                    print(i, end=" ")
                    Suma += i
# Este else para los vacios
                else:
                    print(" ", end=" ")
            print()

except:
    print("Error")