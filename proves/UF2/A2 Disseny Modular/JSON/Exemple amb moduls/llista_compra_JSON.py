import json

def guardar_llista_compra(nom_fitxer, llista_compra):

   """

   Guardar la llista de la compra en un fitxer JSON

   :param nom_fitxer: nom i ruta sensera del fitxer on es vol guardar la llista de la compra

   :param llista_compra: llist de productes, quantitat i marca

   :return: Podria mostrar error en cas de no poder guardar la llista de la compra en un fitxer JSON

   """

   with open(nom_fitxer, "w") as fitxer:

       json.dump(llista_compra, fitxer)

   return ("Llista de la compra guardada al fitxer:", nom_fitxer)







def llegir_llista_compra(nom_fitxer):

   # Llegir la llista de la compra des del fitxer JSON

   with open(nom_fitxer, "r") as fitxer:

       llista_compra = json.load(fitxer)

   return llista_compra





def mostrar_llista_compra(llista_compra):

   llista = "Llista de la compra:\n"

   for item in llista_compra:

       llista = llista + "-----------------------------" + "\n"

       llista = llista + "Producte:\t"+ item["producte"] + "\n"

       llista = llista + "Quantitat:\t" + str(item["quantitat"]) + "\n"

       llista = llista + "Marca:\t:\t" + item["marca"] + "\n"

   return llista