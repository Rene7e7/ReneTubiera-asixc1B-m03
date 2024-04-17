'''
Després de fer un examen un professor vol veure l'estat general de la classe. Vol conèixer la nota mínima, la màxima i la mitjana dels seus alumnes. Les notes provenen d'un fitxer la ruta del qual serà introduïda per teclat. Per tant, la quantitat de notes és indeterminada, i dependrà del contingut de cada fitxer que es faci servir.

Fes un petit programa que li solucioni la tasca (les notes de l'examen no tenen decimals).

El format de l'arxiu student.stats és: 5 3 4 7 8 una sèrie de números sense decimals entre 0 i 10.

student2.stats
'''

def students():
    # variable con la ruta en la que se encuentra el fitxer
    # elegir el fitxer
    try:
        fitxer = "student2.stats"
        # llegir el fitxer

        with open(fitxer, mode='rt', encoding='utf-8') as file:
            notes = file.read()
            notes = notes.split()
            notes = [int(nota) for nota in notes]
            print(f"La nota mínima és: {min(notes)}")
            print(f"La nota màxima és: {max(notes)}")
            print(f"La nota mitjana és: {sum(notes) / len(notes)}")
            print("")
    except FileNotFoundError:
        print("El fitxer no existeix.")
    except ValueError:
        print("El fitxer no conté notes vàlides.")
        # except de no numeros decimales o no entre 0 i 10
    except Exception as e:
        print(e)
        print(" Solo se admiten números enteros entre 0 y 10.")

def error_students():
    try:
        students()
    except Exception as e:
        print(e)
        print("Error en la funció students()")

error_students()

