def llegirPartitsDeTeclat():
    print("<llegirPartitsDeTeclat> ...")
    # Aquí iría la implementación para leer los resultados de los partidos por teclado
    # Por ahora, simplemente simulamos la lectura con un mensaje de impresión
    return [
        {'equip_local': 'Barcelona', 'equip_visitant': 'Real Madrid', 'resultat': '1'},
        {'equip_local': 'Atletico Madrid', 'equip_visitant': 'Sevilla', 'resultat': 'E'},
        {'equip_local': 'Real Madrid', 'equip_visitant': 'Atletico Madrid', 'resultat': '2'},
        {'equip_local': 'Sevilla', 'equip_visitant': 'Barcelona', 'resultat': 'E'},
        {'equip_local': 'Real Madrid', 'equip_visitant': 'Sevilla', 'resultat': '1'},
        {'equip_local': 'Atletico Madrid', 'equip_visitant': 'Barcelona', 'resultat': '2'},
        {'equip_local': 'Barcelona', 'equip_visitant': 'Atletico Madrid', 'resultat': 'E'},
        {'equip_local': 'Sevilla', 'equip_visitant': 'Real Madrid', 'resultat': '2'},
        {'equip_local': 'Atletico Madrid', 'equip_visitant': 'Sevilla', 'resultat': '1'},
        {'equip_local': 'Barcelona', 'equip_visitant': 'Real Madrid', 'resultat': 'E'},
        {'equip_local': 'Real Madrid', 'equip_visitant': 'Barcelona', 'resultat': '2'},
        {'equip_local': 'Sevilla', 'equip_visitant': 'Atletico Madrid', 'resultat': 'E'}
    ]

def quiGuanya(resultat):
    if resultat == 'E':
        return 0
    elif resultat == '1':
        return 1
    elif resultat == '2':
        return -1

def punts(llistaResultats):
    return llistaResultats.count('1') * 3 + llistaResultats.count('E')

def equips(resultatsLliga):
    return set([partit['equip_local'] for partit in resultatsLliga] + [partit['equip_visitant'] for partit in resultatsLliga])

def infoEquips(resultatsLliga, equips):
    info_equips = []
    for equip in equips:
        partits_jugats = [partit for partit in resultatsLliga if partit['equip_local'] == equip or partit['equip_visitant'] == equip]
        partits_guanyats = sum([quiGuanya(partit['resultat']) == 1 for partit in partits_jugats])
        partits_empatats = sum([quiGuanya(partit['resultat']) == 0 for partit in partits_jugats])
        partits_perduts = sum([quiGuanya(partit['resultat']) == -1 for partit in partits_jugats])
        punts_obtinguts = punts([partit['resultat'] for partit in partits_jugats])
        info_equips.append((equip, partits_guanyats, partits_empatats, partits_perduts, punts_obtinguts))
    return info_equips

def classificacio(info_equips):
    return sorted(info_equips, key=lambda x: x[4], reverse=True)

def impClassificacio(resultatsLliga):
    equips_lliga = equips(resultatsLliga)
    info_equips = infoEquips(resultatsLliga, equips_lliga)
    classificacio_equips = classificacio(info_equips)
    print("Classificació de la lliga:")
    print("Pos  Equip    PG  PE  PP  Pts")
    for idx, equip in enumerate(classificacio_equips, start=1):
        print("{:<4} {:<8} {:<3} {:<3} {:<3} {:<3}".format(idx, *equip))

if __name__ == "__main__":
    resultatsLliga = llegirPartitsDeTeclat()
    impClassificacio(resultatsLliga)


