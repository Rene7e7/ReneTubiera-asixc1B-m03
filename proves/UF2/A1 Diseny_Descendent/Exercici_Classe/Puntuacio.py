'''
def analyze_game():
    team1 = input("Enter the name of the first team: ")
    team2 = input("Enter the name of the second team: ")

    team1_score = 0
    team2_score = 0

    while True:
        score = input("Enter the current score (or -1 to end): ")
        if score == "-1":
            break

        score1, score2 = map(int, score.split())
        if score1 > team1_score:
            if score1 - team1_score == 1:
                print(f"Free kick of {team1}")
            elif score1 - team1_score == 2:
                print(f"Basket of {team1}")
            elif score1 - team1_score == 3:
                print(f"Triple of {team1}")
            else:
                print(f"Score of {score1 - team1_score} points by {team1}")

            team1_score = score1
        elif score2 > team2_score:
            if score2 - team2_score == 1:
                print(f"Free kick of {team2}")
            elif score2 - team2_score == 2:
                print(f"Basket of {team2}")
            elif score2 - team2_score == 3:
                print(f"Triple of {team2}")
            else:
                print(f"Score of {score2 - team2_score} points by {team2}")

            team2_score = score2

    if team1_score > team2_score:
        print(f"{team1} wins")
    elif team2_score > team1_score:
        print(f"{team2} wins")
    else:
        print("The game is a draw")

analyze_game()
'''
def equips():
    equipo1 = input("Enter the name of team 1: ")
    equipo2 = input("Enter the name of team 2: ")
    return equipo1, equipo2

def puntuacio():
    puntuacio_equipo1 = 0
    puntuacio_equipo2 = 0
    while True:
        score = input("Enter the current score (or -1 to end): ")
        if score == "-1":
            break
        # Assuming score is a string in the format 'team1:team2'
        score1, score2 = map(int, score.split(':'))
        if score1 > puntuacio_equipo1:
            if score1 - puntuacio_equipo1 == 1:
                print(f"Free kick of {equipo1}")
            elif score1 - puntuacio_equipo1 == 2:
                print(f"Basket of {equipo1}")
            elif score1 - puntuacio_equipo1 == 3:
                print(f"Triple of {equipo1}")
            else:
                print(f"Score of {score1 - puntuacio_equipo1} points by {equipo1}")
            puntuacio_equipo1 = score1
        elif score2 > puntuacio_equipo2:
            if score2 - puntuacio_equipo2 == 1:
                print(f"Free kick of {equipo2}")
            elif score2 - puntuacio_equipo2 == 2:
                print(f"Basket of {equipo2}")
            elif score2 - puntuacio_equipo2 == 3:
                print(f"Triple of {equipo2}")
            else:
                print(f"Score of {score2 - puntuacio_equipo2} points by {equipo2}")
            puntuacio_equipo2 = score2
    return puntuacio_equipo1, puntuacio_equipo2

def guanyador(puntuacio_equipo1, puntuacio_equipo2, equipo1, equipo2):
    if puntuacio_equipo1 > puntuacio_equipo2:
        print(f"{equipo1} wins")
    elif puntuacio_equipo2 > puntuacio_equipo1:
        print(f"{equipo2} wins")
    else:
        print("The game is a draw")

equipo1, equipo2 = equips()
puntuacio_equipo1, puntuacio_equipo2 = puntuacio()
guanyador(puntuacio_equipo1, puntuacio_equipo2, equipo1, equipo2)

