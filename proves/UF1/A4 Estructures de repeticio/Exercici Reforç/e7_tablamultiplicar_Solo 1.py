
numero = int(input("Dime un numero para hacer la tabla de multiplicar: "))
print("--------------")
for j in range(1,10):
    # Imprime la multiplicación de i y j utilizando f-strings
    print(f"{numero} x {j} = {numero*j}")

# Imprime una línea divisoria entre cada tabla de multiplicar
print("--------------")
