
quantitat_euros = int(input("Digam una quantitat de euros: "))
billetera = quantitat_euros

billete_100 = 0
billete_50 = 0
if quantitat_euros >= 500:
    billetera=int(quantitat_euros/500)*500-quantitat_euros
    print()
else:
    billetera=int(quantitat_euros/100)*100-quantitat_euros
    billete_100=quantitat_euros/100
    print("Ha gastat", billete_100, " de 100 euros")




