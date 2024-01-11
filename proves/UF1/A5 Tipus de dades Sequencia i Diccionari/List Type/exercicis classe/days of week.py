'''
Rene Tubiera
DayOfWeek
'''




try:
    diasCAT = ["Dilluns", "Dimarts", "Dimercres", "Dijous", "Divendres", "dissabte", "Diumenge"]
    diasENG = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    diasESP = ["Lunes", "Martes", "Dimercros", "Jueves", "Viernes", "sábado", "Domingo"]

    usuaris = int(input())
    if usuaris >= 1 and usuaris <= 7:
        print(diasCAT[usuaris-1], diasESP[usuaris-1], diasENG[usuaris-1])
    else:
        print("Nomes un numer del 1 al 7")


except ValueError:
    print("Error")