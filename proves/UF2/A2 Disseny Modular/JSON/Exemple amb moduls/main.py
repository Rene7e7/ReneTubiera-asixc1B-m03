import llistaCompra_JSON as compra



# Llista de la compra amb els productes, quantitat i marca

llista_compra = [

   {"producte": "pomes", "quantitat": 3, "marca": "marca_A"},

   {"producte": "plàtans", "quantitat": 5, "marca": "marca_B"},

   {"producte": "llet", "quantitat": 1, "marca": "marca_C"},

   {"producte": "pa", "quantitat": 2, "marca": "marca_D"}

]

nom_fitxer = "llista_compra.json"



resultat = compra.guardar_llista_compra(nom_fitxer, llista_compra)

print(resultat)

compra.llegir_llista_compra(nom_fitxer)

llista = compra.mostrar_llista_compra(llista_compra)

print(llista)