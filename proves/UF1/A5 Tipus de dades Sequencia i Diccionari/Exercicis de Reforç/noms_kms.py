'''
e13.py
D'una empresa de transport es vol guardar el nom dels conductors que hi treballa, i els quilòmetres que condueixen cada dia de la setmana.
Per desar aquesta informació es faran servir dues llistes:
noms: Llista per desar els noms dels conductors.
kms: Taula on a cada posició hi ha els kms que un conductor ha fet a cadascú dels dies de la setmana.
Exemple de valors a les dues llistes:
noms = [Eva, Carles, Júlia]
kms = [
[100,230,90,150,80,115,75],  # kms fets per Eva durant la setmana
[90,210,70,50,180,150,175] , # kms fets per Carles durant la setmana
 [220,160,170,90,70,250,120] # kms fets per Julia durant la setmana
]
El programa procedirà de la manera següent. Primer demanarà per teclat:
 els noms de cada conductor
per a cada conductor, els kms de cada dia de la setmana
A continuació, el programa generarà una nova llista (“total_kms”) amb els quilòmetres totals que ha recorregut cada conductor durant la setmana.
Finalment, el programa mostrarà per pantalla la llista amb els noms de conductors i els quilòmetres setmanals que ha fet.

'''

noms_lista = []
kms_lista = []

try:
    for _ in range(3):
        nom_conductor = input("Introduce el nombre del conductor: ")
        noms_lista.append(nom_conductor)

        kms_semana = []
        for _ in range(2):
            kms_dia = int(input(f"Introduce los kilómetros para {nom_conductor} el día {_ + 1}: "))
            kms_semana.append(kms_dia)

        kms_lista.append(kms_semana)

    # Calcular la lista con los kilómetros totales por conductor
    total_kms = [sum(kms_semana) for kms_semana in kms_lista]


    # Mostrar la lista con nombres de conductores y kilómetros semanales
    for i in range(len(noms_lista)):
        if i < len(total_kms):
            print(f"{noms_lista[i]}: {total_kms[i]} km semanales")
        else:
            print(f"{noms_lista[i]}: 0 km semanales")

except ValueError:
    print("Error: Por favor, introduce un valor numérico válido para los kilómetros.")
