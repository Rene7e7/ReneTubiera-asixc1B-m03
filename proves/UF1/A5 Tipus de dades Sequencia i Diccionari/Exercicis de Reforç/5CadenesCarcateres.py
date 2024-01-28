'''
e2.py
Crea una llista i inicialitza-la amb 5 cadenes de caràcters llegides
per teclat. Copia els elements de la llista a una altra llista però
en ordre invers, i mostra els elements d'aquesta segona llista per
pantalla.

'''
# e2.py

# Crear una llista i inicialitzar-la amb 5 cadenes llegides per teclat
llista_original = []
for i in range(5):
    cadena = input(f"Introdueix la cadena {i + 1}: ")
    llista_original.append(cadena)

# Copiar els elements de la llista original a una altra llista en ordre invers
llista_inversa = list(reversed(llista_original))

# Mostrar els elements de la segona llista per pantalla
print("Llista original:", llista_original)
print("Llista inversa:", llista_inversa)
