'''
e3.py
Es vol fer un programa que llegeixi per teclat les 5 notes
obtingudes per un alumne (s’ha de validar que els notes estiguin
compreses entre 0 i 10). A continuació heu de mostrar totes les notes,
 la nota mitjana, la nota més alta que ha tret i la menor.
Pista: max , min, sum,  len

'''

llista_notes = []
for i in range(5):
    notes = int(input("Digam 5 notes: "))
    llista_notes.append(notes)
    if 0 <= notes <= 10:
        print(max(llista_notes))
        print(min(llista_notes))
        print(sum(llista_notes)/5)


