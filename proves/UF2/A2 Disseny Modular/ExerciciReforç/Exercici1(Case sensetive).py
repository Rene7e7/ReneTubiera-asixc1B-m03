'''
Dissenya modularment una aplicació que permet extreure informació del fitxer de “log” que se li suministri.

Nota: donat que encara no hem après com llegir fitxers amb Python, les funcions que implementin la funcionalitat de llegir un fitxer, les simuleu amb l’entrada de text per teclat.

L’aplicació ha de poder fer les següents accions:
llegir un fitxer de text (la ruta i el nom del fitxer els proporcionarà l’usuari)
demanar una paraula a l’usuari i si la cerca ha de ser “case sensitive” o no.
cercar en el fitxer una paraula:
mostrar les línies que contenen una paraula donada en qualsevol posició de la línia
mostrar les línies que comencen amb una paraula donada
mostrar les línies que acaben amb una paraula donada
comptar quantes vegades apareix dins del fitxer:
una paraula en qualsevol posició de qualsevol línia del fitxer
una paraula al començament de qualsevol línia del fitxer
una paraula al final de qualsevol línia del fitxer
mostrar les estadístiques del recompte de:
quantes vegades apareix dins del fitxer, en qualsevol posició, la paraula entrada per l’usuari
quantes vegades apareix dins del fitxer, al començament de línia, la paraula entrada per l’usuari
quantes vegades apareix dins del fitxer, al final de línia, la paraula entrada per l’usuari
en qualsevol estadística s’ha de mostrar la paraula buscada, la ruta i el nom del fitxer i si la cerca ha sigut “case sensitive” o “case insensitive”.

La pantalla per a mostrar les estadístiques ha de tenir un aspecte similar al següent (suposeu que l’usuari ha demanat buscar la paraula “ERROR” al fitxer “/var/log/boot.log”, sense importar si l’ús o no de majúscules o minúscules, “case insensitive”)

'''

# Llegir un fitxer de text
def llegir_fitxer():
    ruta_fitxer = input("Introdueix la ruta i el nom del fitxer: ")
    return ruta_fitxer

# Demanar una paraula a l'usuari i si la cerca ha de ser "case sensitive" o no
def demanar_paraula():
    paraula = input("Introdueix la paraula a cercar: ")
    case_sensitive = input("La cerca ha de ser case sensitive (s/n)? ")
    return paraula, case_sensitive

# Cercar en el fitxer una paraula
def cercar_paraula(ruta_fitxer, paraula, case_sensitive):
    # Obrir el fitxer
    with open(ruta_fitxer, "r") as fitxer:
        # Llegir el fitxer línia per línia
        for linia in fitxer:
            # Eliminar el salt de línia
            linia = linia.rstrip()
            # Comprovar si la paraula apareix a la línia
            if case_sensitive == "s":
                if paraula in linia:
                    print(linia)
            else:
                if paraula.lower() in linia.lower():
                    print(linia)

# Comptar quantes vegades apareix dins del fitxer una paraula
def comptar_paraula(ruta_fitxer, paraula, case_sensitive):
    # Inicialitzar els comptadors
    total = 0
    comencament = 0
    final = 0
    # Obrir el fitxer
    with open(ruta_fitxer, "r") as fitxer:
        # Llegir el fitxer línia per línia
        for linia in fitxer:
            # Eliminar el salt de línia
            linia = linia.rstrip()
            # Comprovar si la paraula apareix a la línia
            if case_sensitive == "s":
                if paraula in linia:
                    total += 1
                if linia.startswith(paraula):
                    comencament += 1
                if linia.endswith(paraula):
                    final += 1
            else:
                if paraula.lower() in linia.lower():
                    total += 1
                if linia.lower().startswith(paraula.lower()):
                    comencament += 1
                if linia.lower().endswith(paraula.lower()):
                    final += 1
    # Mostrar les estadístiques
    print(f"La paraula buscada és '{paraula}', la ruta i el nom del fitxer és '{ruta_fitxer}' i la cerca és {'case sensitive' if case_sensitive == 's' else 'case insensitive'}:")
    print(f"Total: {total}")
    print(f"Començament: {comencament}")
    print(f"Final: {final}")

# Programa principal
ruta_fitxer = llegir_fitxer()
paraula, case_sensitive = demanar_paraula()
cercar_paraula(ruta_fitxer, paraula, case_sensitive)
comptar_paraula(ruta_fitxer, paraula, case_sensitive)
