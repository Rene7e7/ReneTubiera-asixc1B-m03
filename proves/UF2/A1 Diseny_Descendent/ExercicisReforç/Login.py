'''
Crear un programa  on es demani un nom d'usuari i una contrasenya i la quantitat  d’intents per fer login.
Si l’usuari encerta la combinació de nom d’usuari i
contrasenya, el programa li mostrarà el missatge “Benvingut al Sistema!” i una foto de la seva cara feta amb caràcters
 ASCII.
En cas contrari, el programa li mostrarà un missatge d’error (“Error: Nom d'usuari o contrasenya errònia!”) i tornarà a demanar-li les dades.
Si després dels intents, l’usuari no l’encerta, el programa mostrarà el missatge “Error: s’ha esgotat el nombre
d’intents!” i acabarà.
Crear, com a mínim,  una funció anomenada “setLogin”, que rep tres paràmetres:
nomUsuari: el nom d'usuari que vol fer “login”
contrasenya: la contrasenya que es vol fer servir per fer “login” amb l’usuari donat
intents: el nombre d’intents dels que es disposa per a fer login
Si els valors passats com a paràmetre són “usuari1” per al nom d'usuari i “asdasd” per a la contrasenya, aleshores
la funció retorna True i el nombre d’intents tal qual. En cas contrari, la funció retorna False i el valor dels
intents restants
v2.0: Multiusuari. mínim 2 max 10 usuaris diferents.
v3.0: Password validator: Les contrasenyes han de complir els requisits de complexitat
'''
def setLogin(nomUsuari, contrasenya, intents):
    usuaris = {
        "usuari1": "asdasd",
        "usuari2": "qwerty",
        "usuari3": "123456",
        "usuari4": "password",
        "usuari5": "1234",
    }

    if nomUsuari in usuaris and usuaris[nomUsuari] == contrasenya:
        return True, intents
    else:
        return False, intents - 1

def main():
    intents = 3
    while intents > 0:
        nomUsuari = input("Introdueix el nom d'usuari: ")
        contrasenya = input("Introdueix la contrasenya: ")
        login, intents = setLogin(nomUsuari, contrasenya, intents)
        if login:
            print("Benvingut al Sistema!")
            # Vols crear un usuari?
            CreateUsers()
        else:
            print("Error: Nom d'usuari o contrasenya errònia!")
    else:
        print("Error: s'ha esgotat el nombre d'intents!")

def CreateUsers():
    usuaris = {}
    while True:
        try:
            n = int(input("Introdueix el nombre d'usuaris: "))
            break
        except ValueError:
            print("Error: Introdueix un nombre vàlid d'usuaris.")

    for i in range(n):
        nom = input("Introdueix el nom de l'usuari: ")
        password = input("Introdueix la contrasenya: ")
        if validatePassword(password):
            usuaris[nom] = password
        else:
            print("La contrasenya no compleix els requisits de complexitat")
    print(usuaris)


def validatePassword(password):
    if len(password) < 8:
        return False
    if not any(c.isupper() for c in password):
        return False
    if not any(c.islower() for c in password):
        return False
    if not any(c.isdigit() for c in password):
        return False
    return True

if __name__ == "__main__":
    main()


