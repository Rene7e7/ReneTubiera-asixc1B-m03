"""
11/10/2023
René Tubiera y Jordi Yu

E2.  AirVolumeCalculator
Per poder fer un estudi de la ventilació d'una aula necessitem poder calcular la quantitat d'aire que hi cap en una habitació.
Llegeix les 3 dimensions de l'aula i mostra per pantalla quin volum té.
Cal mostrar per pantalla: “El volum de l’aula és xxx m3”
"""
# Pedimos a l'usuario un numero a la altura, anchura i longitud
Altura = int(input("Dime la altura de la aula: "))
Anchura = int(input("Dime la anchura de la aula: "))
Longitud = int(input("Dime la longitud de la aula: "))
# Creamos un variable que hace el calculo del volumen
Volumen = Altura*Anchura*Longitud
print("El volum de l’aula és ", Volumen, "m³")