'''
Crear un programa per gestionar els resultats de la travessa de futbol. Per això utilitzarem dues taules:
Equips: Que és una taula de cadenes on guardem a cada columna el nom dels equips de cada partit. A la travessa s'indiquen 15 partits.
Resultats: És una taula d'enters on s'indica el resultat. També té dues columnes, a la primera es guarda el nombre de gols de l'equip que està guardat a la primera columna de la taula anterior, i a la segona els gols de l'altre equip.
El programa anirà demanant els noms dels equips de cada partit i el resultat del partit, tot seguit s'imprimeix la travessa d'aquesta jornada.
Quina modificació caldria fer a les taules per guardar tots els resultats de totes les jornades de la temporada?

'''
# Inicializar las listas de equipos y resultados
equips = []
resultats = []

# Bucle para gestionar els resultats de la travessa
for jornada in range(1, 16):
    print(f"\nJornada {jornada}:")

    # Inicializar listas para la jornada actual
    equips_jornada = []
    resultats_jornada = []

    # Bucle para demanar noms dels equips i resultats de cada partit
    for partit in range(1, 16):
        equip_local = input(f"Nom de l'equip local per al partit {partit}: ")
        equip_visitant = input(f"Nom de l'equip visitant per al partit {partit}: ")

        # Demanar el resultat del partit
        gols_local = int(input(f"Gols de {equip_local}: "))
        gols_visitant = int(input(f"Gols de {equip_visitant}: "))

        # Guardar noms d'equips i resultats de la jornada actual
        equips_jornada.append(equip_local)
        equips_jornada.append(equip_visitant)
        resultats_jornada.append(gols_local)
        resultats_jornada.append(gols_visitant)

    # Guardar les llistes de la jornada actual a les llistes globals
    equips.append(equips_jornada)
    resultats.append(resultats_jornada)

# Imprimir la travessa de la temporada
for jornada in range(1, 16):
    print(f"\nJornada {jornada}:")
    index_inicio = (jornada - 1) * 30
    index_fin = jornada * 30

    for partit in range(index_inicio, index_fin, 2):
        equip_local = equips[jornada - 1][partit]
        equip_visitant = equips[jornada - 1][partit + 1]
        gols_local = resultats[jornada - 1][partit]
        gols_visitant = resultats[jornada - 1][partit + 1]
        print(f"Partit {partit // 2 + 1}: {equip_local} {gols_local}-{gols_visitant} {equip_visitant}")




