""""
Programa que demana l'import d'una factura, amb iva inclòs. Calcula l'import amb descompte, en cas de tenir la targeta de
client, tenint en compte els següents criteris:
Si l'import de la factura, és igual o superior a 100 €, se li aplica un descompte del 21%,
en cas contrari no se li aplica cap descompte. El descompte es calcula al preu final,  i no a la “base imponible”.
I després si li aplica l’IVA . Precio total = Base imponible * Tipo de IVA
"""

Factura = int(input("Dime la factura: "))
IVA = 0.21
PreuTotal = Factura + IVA
if Factura <= 100:
    FacturaIVAconDesc = Factura / IVA + Factura
    print("El preu total amb decompte es: ", FacturaIVAconDesc)
else:
    print("El Preu total sense descompte: ", PreuTotal)





