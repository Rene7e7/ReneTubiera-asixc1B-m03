Usuaris = {
    "admin": "admin",
    "user1": "user1",
    "user2": "user2",
    "user3": "user3",
    "user4": "user4",
    "choper": "choper"
}
def SetLogin():
    usuari = input("Usuari: ")
    contrasenya = input("Contrasenya: ")
    return usuari, contrasenya
def Login(usuari, contrasenya):
    if usuari in Usuaris:
        if Usuaris[usuari] == contrasenya:
            print("Benvingut")
            exit()
        else:
            print("Contrasenya incorrecta")
    else:
        print("Usuari incorrecte")
usuari, contrasenya = SetLogin()

def intents(usuari, contrasenya):
    intents = 3
    while intents > 0:
        if usuari in Usuaris:
            if Usuaris[usuari] == contrasenya:
                print("Benvingut")
                exit()
            else:
                print("Contrasenya incorrecta")
                intents -= 1
                print(f"Et queden {intents} intents")
                usuari, contrasenya = SetLogin()
        print(f"Et queden {intents} intents")
    print("Has esgotat els intents")
    exit()




