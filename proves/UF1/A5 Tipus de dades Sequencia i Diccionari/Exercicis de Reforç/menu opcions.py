'''
e16.py
Crearem un programa amb un menú d'opcions que implementi les funcionalitats següents sobre una llista:
Afegir número a la llista: es demana un número per teclat i és és afegit al final de la llista.
Afegir número de la llista en una posició: es demana un número i una posició, i si la posició existeix a la llista, el programa insereix el número a la llista a la posició indicada. L'usuari ha d'entrar les posicions com a números a partir de l'1, incloent-hi.
Longitud de la llista: mostra el nombre d'elements de la llista.
Suprimeix el darrer número: mostra l'últim número de la llista i l'esborra.
Suprimeix un número: Demana una posició, i si la posició existeix a la llista l'esborra (la posició entrada ha de ser un número partir de l'1).
Comptar números: Et demana un número i et diu quantes aparicions n'hi ha a la llista.
Posicions d'un número: Et demana un número i et diu quines posicions de la llista està (les posicions es comptaran des del 1).
Mostrar números: Mostra els números de la llista.
Sortir del programa.

'''
llista_numero = [5, 5, 4, 2]

# Afegir número a la llista
numero = int(input("Dime un número: "))
llista_numero.append(numero)
print("Número afegit a la llista.")

# Afegir número de la llista en una posició
posicio = int(input("Entra la posició (a partir de 1): "))
if 1 <= posicio <= len(llista_numero) + 1:
    numero = int(input("Dime un número: "))
    llista_numero.insert(posicio - 1, numero)
    print("Número afegit a la llista a la posició indicada.")
    print("Llista després de la inserció:", llista_numero)
else:
    print("Posició no vàlida. La posició ha d'estar entre 1 i", len(llista_numero) + 1)

# Longitud de la llista
print("Longitud de la llista:", len(llista_numero))

# Suprimeix el darrer número
if len(llista_numero) > 0:
    ultim_numero = llista_numero.pop()
    print("Últim número:", ultim_numero)
    print("Llista després de suprimir l'últim número:", llista_numero)
else:
    print("La llista està buida. No es pot suprimir cap número.")

# Suprimeix un número
if len(llista_numero) > 0:
    posicio = int(input("Entra la posició (a partir de 1): "))
    if 1 <= posicio <= len(llista_numero):
        llista_numero.pop(posicio - 1)
        print("Llista després de suprimir el número:", llista_numero)
    else:
        print("Posició no vàlida. La posició ha d'estar entre 1 i", len(llista_numero))

# Comptar números
if len(llista_numero) > 0:
    num = int(input("Entra un número: "))
    aparicions = llista_numero.count(num)
    print(f"El número {num} apareix {aparicions} vegades a la llista.")

# Posicions d'un número
if len(llista_numero) > 0:
    num = int(input("Entra un número: "))
    posicions = [i + 1 for i, x in enumerate(llista_numero) if x == num]
    if posicions:
        print(f"El número {num} es troba a les posicions {', '.join(map(str, posicions))} de la llista.")
    else:
        print(f"El número {num} no es troba a la llista.")
