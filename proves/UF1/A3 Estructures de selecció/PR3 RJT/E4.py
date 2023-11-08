""""
Programa que demana l'import d'una factura, amb iva inclòs. Calcula l'import amb descompte,
en cas de tenir la targeta de
client, tenint en compte els següents criteris:
Si l'import de la factura, és igual o superior a 100 €, se li aplica un descompte del 21%,
en cas contrari no se li aplica cap descompte. El descompte es calcula al preu final,  i no a la “base imponible”.
I després si li aplica l’IVA . Precio total = Base imponible * Tipo de IVA
"""

Factura = int(input("Dime la factura: "))
IVA = Factura * 0.21
PreuTotal = Factura + IVA
FacturaIVAconDesc = PreuTotal - PreuTotal * 0.21
if Factura >= 100:
    print("El preu total amb decompte es: ", round(FacturaIVAconDesc))
else:
    print("El Preu total sense descompte: ", round(PreuTotal))
