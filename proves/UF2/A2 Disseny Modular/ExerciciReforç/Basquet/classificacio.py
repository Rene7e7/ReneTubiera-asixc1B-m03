'''
Crea una aplicació “Lliga”, la qual permet mostrar en pantalla la classificació de la lliga de futbol a partir dels resultats de tots els partits que s’han disputat fins un moment donat.
Nota: En aquest cas, cal implementar tota la funcionalitat de l’aplicació, tret de la part que s’ocupa de la lectura del fitxer de text amb els resultats de la lliga (veure més endavant)

Dissenyeu els mòduls que componen l’aplicació, tenint en compte que tindrem les següents funcions:
llegirPartitsDeFitxer(rutaFitxer): Funció que llegeix el fitxer CSV amb els resultats de tots els partits jugats fins el moment. El nom del fitxer, inclouent la ruta al seu directori, és passat per paràmetre. Torna les dades dels resultats dels partits jugats de la lliga en una llista de diccionaris.
llegirPartitsDeTeclat(): Funció que demana per teclat els resultats de tots els partits jugats fins el moment. Torna les dades dels resultats dels partits jugats de la lliga en una llista de diccionaris.
Nota: donat que encara no hem après com llegir fitxers amb Python, només cal implementar llegirPartitsDeTeclat, la funció , només tindrà una implementació simulada (un print de l’estil “print(“<llegirPartitsDeFitxer> …”)“

impClassificacio(resultatsLliga):Rep la llista de diccionaris generat a partir de la funció anterior, genera les dades de la classificació i les mostra per pantalla.
La funció “impClassificacio” fa servir internament les següents funcions:
equips(resultatsLliga): Funció que rep la llista de diccionaris amb els resultats dels partits jugats de la lliga i torna un conjunt amb els equips de la lliga.
infoEquips (resultatsLliga, equips): Funció que rep la llista de diccionaris amb els resultats dels partits jugats de la lliga i el conjunt d'equips i torna una llista de tuples, a cada tupla es guarda un equip amb els partits guanyats, empatats i perduts i els punts obtinguts.
classificacio() : Funció que rep la llista de tuples generada per “infoEquips” i l’ordena segons el nombre de punts de cada element de la llista (cada tupla amb nom d’equip i els seus punts)
La funció “infoEquips”, al seu turn, fa servir:
quiGuanya(resultat): Funció que rep un resultat i torna un 0 si és un empat, un 1 si guanya l'equip de casa i -1 si guanya l'equip visitant.
punts(llistaResultats): Funció que rep una llista amb els partits guanyats, empatats i perduts i torna els punts obtinguts.

'''

