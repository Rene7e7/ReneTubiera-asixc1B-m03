'''
Crear una funció no recursiva que permeti calcular el factorial d'un número. Realitza un programa principal on es llegeixi
 un sencer i es mostri el resultat del factorial.
Fel mateix amb una funció recursiva.
Tip: Factorial
Resum estret de la Viquipèdia:
En matemàtiques, el factorial d’un enter no negatiu, denotat amb “n!”,  és el producte de tots els nombres enters positius
iguals o inferiors a n. És a dir:
n! = 1 x 2 x 3 … x (n-1) x n
Per convenció, 0! = 1
Per exemple:
5! = 1 x 2 x 3 x 4 x 5 = 120

'''

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

def factorialRecursiu(n):
    if n == 0:
        return 1
    return n * factorialRecursiu(n - 1)

def main():
    n = int(input("Introdueix un número: "))
    print(f"El factorial de {n} és {factorial(n)}")
    print(f"El factorial de {n} és {factorialRecursiu(n)}")

if __name__ == "__main__":
    main()
