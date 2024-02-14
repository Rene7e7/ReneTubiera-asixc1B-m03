
def analyze_game():
    team1 = input("")
    team2 = input("")

    team1_score = 0
    team2_score = 0

    while True:
        score = input("")
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
