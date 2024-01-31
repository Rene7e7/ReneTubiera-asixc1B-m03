'''
indica si una paraula o frase és palíndrom.


Exemples de palíndroms:

cec, cuc, gag, mínim, nan, nen, pipiripip…



Paslindroms en català

I Paco pagès sega poc api.

Mig el llegim

Set penis ineptes.

Un aviador roda i va nu


Palíndromos del castellano : Acurruca, Roma

Amo la pacífica paloma

Sobornos son robos

Nada, yo soy Adán

Amigo, no gima

Amad a la dama.



Palindorms en Anglès: civic, level, radar, Hannah, Leveler

Madam, in Eden, I’m Adam

A man, a plan, a canal, Panama

Star rats.

1 Obtenir dades
2 neteja ( min / maj, accents, Espais )
3 Girar i comparar
'''



palindrom = input("Posa una paraula o una frase: ")
palindrom = palindrom.lower().strip(" ")
palindrom = palindrom.replace(" ", "")

if palindrom == palindrom[::-1]:
    print("Es un palindrom")
else:
    print("No es un palindrom")

print(palindrom)





