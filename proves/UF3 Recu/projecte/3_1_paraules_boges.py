import random
import string

def desordenar_paraula(paraula):
    if len(paraula) <= 2:
        return paraula
    primer = paraula[0]
    ultim = paraula[-1]
    mig = list(paraula[1:-1])
    random.shuffle(mig)
    return primer + ''.join(mig) + ultim

def detectar_caracters_especials(paraula):
    caracters_especials = []
    for lletra in paraula:
        if lletra in string.punctuation:
            caracters_especials.append(lletra)
    return caracters_especials

def desordenar_frase(frase):
    paraules = frase.split()
    frase_desordenada = []
    caracters_especials = []
    for paraula in paraules:
        paraula_caracters_especials = detectar_caracters_especials(paraula)
        if paraula_caracters_especials:
            caracters_especials.extend(paraula_caracters_especials)
            frase_desordenada.append(paraula)
        else:
            frase_desordenada.append(desordenar_paraula(paraula))
    return ' '.join(frase_desordenada), caracters_especials

frase = input("Introdueix una frase: ")
frase_desordenada, caracters_especials = desordenar_frase(frase)
print("Frase desordenada:", frase_desordenada)

# Imprimir els caràcters especials en el seu lloc original
print("Caràcters especials:", ''.join(caracters_especials))
