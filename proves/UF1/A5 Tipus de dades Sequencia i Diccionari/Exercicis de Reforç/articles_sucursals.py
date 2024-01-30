'''
e14.py
Crear un programa que llegeixi els preus de 5 articles i les quantitats venudes per una empresa a les seves 3 sucursals. El programa demanarà per teclat:
Els preus de cada article
La quantitat de cada article venut a cada sucursal
A partir de les dades anteriors el programa calcularà i mostrarà per pantalla:
Per cada article, quantes unitats s'han venut en total
La quantitat d'articles venuts a la sucursal 2
La quantitat de l'article 3 venut a la sucursal 1
La recaptació total de cada sucursal
La recaptació total de l’empresa
La sucursal de més recaptació
Pista: podeu fer servir les funcions sum i max de Python.

'''

quantitat = 0
sucursal1 = []
sucursal2 = []
sucursal3 = []
llista_compra = []
recapitacio_total = []
recapitacio_mes = []

while quantitat != 5:
    for i in range(5):
        article = input("Que quieres comprar")
        llista_compra.append(article)
        quantitat += 1
        preu = int(input(f"Dime precio de la {quantitat}a Compra: "))
        llista_compra.append(preu)
        recapitacio_total.append(preu)
        sucursal = int(input("Que sucursal esta? "))
        if sucursal == 1:
            compra = []
            compra.append(sucursal1)
            sucursal1.append(article)
            sucursal1.append(preu)
        print(sucursal1)
        if sucursal == 2:
            compra = []
            compra.append(sucursal2)
            sucursal2.append(article)
            sucursal2.append(preu)
        print(sucursal2)
        if sucursal == 3:
            compra = []
            compra.append(sucursal3)
            sucursal3.append(article)
            sucursal3.append(preu)
        print(sucursal3)
print("Recapitacion total de la empresa", sum(recapitacio_total))
print("Recapitacion de mes recapitacio", max(sucursal1))

'''
Compra
    Sucursal 1
    - nombreCliente
    - Precio
    Sucursal 2
    - nombreCliente
    - Precio
    Sucursal 3
    - nombreCliente
    - Precio 
'''

