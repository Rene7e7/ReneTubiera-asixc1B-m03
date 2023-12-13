print(" Literatura,Cinema,Muisca, Videojocs, Sortir")
try:
    usuario = input("Que quieres saber? ")
    Sortir = "Sortir"
    match usuario.capitalize():
        case 1:
            print("Catalan, Latin, Ingles.")
        case 2:
            print("Avengers, Aquaman, Marvel")
        case 3:
            print("Pop, K-pop, Rock")
        case 4:
            print("Valorant, LOL, Pokemon")
        case 5:
            print("ADIOS ")
        case 6:
            print()

except ValueError:
    print("Error")
