"""
11/10/2023
René Tubiera y Jordi Yu

E4. WorkingAge
Escriu un programa que llegeixi l'edat de l'usuari i mostri si té edat per treballar, l'edat mínima per treballar legalment és 16 i suposarem l'edat màxima als 65.
"""
# Pedimos a l'usuario que ponga un numero de edad
Edat = int(input("Que edad tienes? "))
# Verifica que si es mayor d'edat i que tenga menos de 65 años
if Edat >= 16 and Edat <= 65:
    print("Puedes entrar")
# Pero si no los tiene nos muestra un mensaje que "No puedes entrar"
else:
    print("No puedes entrar")