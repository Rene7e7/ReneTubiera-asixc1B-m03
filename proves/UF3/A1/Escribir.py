# region Escribir
NOM_FITXER="poble1.txt"
try:
    l=[1,2,3,4,5,6]
    f = open(NOM_FITXER, mode='wt', encoding='utf-8')
    resultat=f.write('La mare era mestra.\nSoy ')
    print(resultat)
    resultat=f.write('Vivíem tots dos sols. No teníem ni vàter.\nDamunt de la casa, les estrelles')
    print(resultat)
    f.write("\n"+str(l))
    f.close()
except FileNotFoundError:
    print("Fitxer/Directory no trobat:" + NOM_FITXER)
# endregion
