'''
Crear una funció no recursiva  que calculi el MCD (Màxim Comú Divisor) de dos números pel mètode d'Euclides.
El mètode d'Euclides és el següent:
Es divideix el nombre més gran entre el més petit.
Si la divisió és exacta, el divisor és el MCD.
Si la divisió no és exacta, dividim el divisor entre la resta obtinguda i es continua així fins a obtenir una divisió exacta,
essent el darrer divisor el MCD.
Crea un programa principal que llegeixi dos nombres sencers i mostri el MCD.

'''

def mcd(num1, num2):
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    return num1

def main():
    num1 = int(input("Introdueix el primer número: "))
    num2 = int(input("Introdueix el segon número: "))
    print(f"El MCD és {mcd(num1, num2)}")

if __name__ == "__main__":
    main()
