def equips():
    equipo1 = input("")
    equipo2 = input("")
    return equipo1, equipo2

def puntuacio(equipo1, equipo2):
    puntuacio_equipo1 = 0
    puntuacio_equipo2 = 0
    while True:
        score = input("")
        if score == "-1":
            break
        # Assuming score is a string in the format 'team1:team2'
        score1, score2 = map(int, score.split(' '))
        if score1 > puntuacio_equipo1:
            if score1 - puntuacio_equipo1 == 1:
                print(f"Lliure de {equipo1}")
            elif score1 - puntuacio_equipo1 == 2:
                print(f"Cistella de {equipo1}")
            elif score1 - puntuacio_equipo1 == 3:
                print(f"Triple de {equipo1}")
            puntuacio_equipo1 = score1
        elif score2 > puntuacio_equipo2:
            if score2 - puntuacio_equipo2 == 1:
                print(f"Lliure de {equipo2}")
            elif score2 - puntuacio_equipo2 == 2:
                print(f"Cistella de {equipo2}")
            elif score2 - puntuacio_equipo2 == 3:
                print(f"Triple de {equipo2}")
            puntuacio_equipo2 = score2
    return puntuacio_equipo1, puntuacio_equipo2

def guanyador(puntuacio_equipo1, puntuacio_equipo2, equipo1, equipo2):
    if puntuacio_equipo1 > puntuacio_equipo2:
        print(f"Guanya {equipo1}")
    elif puntuacio_equipo2 > puntuacio_equipo1:
        print(f"Guanya {equipo2}")
    else:
        print("Empat")

equipo1, equipo2 = equips()
puntuacio_equipo1, puntuacio_equipo2 = puntuacio(equipo1, equipo2)
guanyador(puntuacio_equipo1, puntuacio_equipo2, equipo1, equipo2)
