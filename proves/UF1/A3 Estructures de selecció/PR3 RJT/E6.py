"""
L'usuari introdueix la lletra del tipus d'habitatge i número de m3  d'aigua gastats.
Mostrar per pantalla el preu total de la factura de l’aigua. Arrodonit a 2 decimals
El preu que pagues per l’aigua (aigües BCN 2021) que consumeixes.
El consum es divideix en 5 trams de preus progressius. El consum es calcula segons els m3 consumits.
Qui més estalvi d’aigua fa, menys trams consumeix i, per tant, més estalvia.
Aquest sistema ajuda a fomentar un consum responsable. Preu = (5.0 * 0.5849) + 6.40

"""

Letra_tipus_habitatge = input("Tria una opcio: ")
match Letra_tipus_habitatge:
    case "A":
        quota_fixa = 2.46
    case "B":
        quota_fixa = 6.40
    case "C":
        quota_fixa = 7.25
    case "D":
        quota_fixa = 11.21
    case "E":
        quota_fixa = 12.10
    case "F":
        quota_fixa = 17.28
    case "G":
        quota_fixa = 28.01
    case "H":
        quota_fixa = 40.50
    case "I":
        quota_fixa = 61.31
numero_tram = int(input("Tria numero de tram: "))
match numero_tram:
    case 1:
        valor_tram = 0.5849
    case 2:
        valor_tram = 0.5849
    case 3:
        valor_tram = 0.5849
    case 4:
        valor_tram = 0.5849
    case 5:
        valor_tram = 0.5849
    case 6:
        valor_tram = 0.5849
    case 7:
        valor_tram = 1.1699
    case 8:
        valor_tram = 1.1699
    case 9:
        valor_tram = 1.1699
    case 10:
        valor_tram = 1.7548
    case 11:
        valor_tram = 1.7548
    case 12:
        valor_tram = 1.7548
    case 13:
        valor_tram = 1.7548
    case 14:
        valor_tram = 1.7548
    case 15:
        valor_tram = 1.7548
    case 16:
        valor_tram = 2.3397
    case 17:
        valor_tram = 2.3397
    case 18:
        valor_tram = 2.3397
    case 19:
        valor_tram = 2.9246
if numero_tram > 1 or numero_tram <= 19:
    precio = numero_tram * valor_tram + quota_fixa
    print("El precio total es: ", round(precio))
