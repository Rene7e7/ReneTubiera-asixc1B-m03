cont = 0
sortir = False
while not sortir:
   cont = cont + 1
   print(cont)
   opcio = input("Sortir? (s/n): ")
   if opcio.lower() == "s":
       sortir = True
print("Has sortit ... ets lliure ;-)")
