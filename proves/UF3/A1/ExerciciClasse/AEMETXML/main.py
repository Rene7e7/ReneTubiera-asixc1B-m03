import AEMETxml as dades

arxiu = 'localidad_17202.xml'

def main(arxiu):
    try:
        precipitacio, temperatura = dades.parseXML(arxiu)
        print(f'Probabilitat de precipitació: {precipitacio}')
        print(f'Temperatura mitjana: {temperatura}')
    except:
        print('Error en la lectura del fitxer')

main(arxiu)

