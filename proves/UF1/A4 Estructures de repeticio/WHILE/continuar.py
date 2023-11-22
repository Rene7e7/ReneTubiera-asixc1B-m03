cont = 0
continuar = True
while continuar == True:
   cont = cont + 1
   print(cont)
   opcio = input("Continuar? (s/n): ")
   if opcio.lower() == "s":
       continuar = False
print("Has sortit ... ets lliure ;-)")