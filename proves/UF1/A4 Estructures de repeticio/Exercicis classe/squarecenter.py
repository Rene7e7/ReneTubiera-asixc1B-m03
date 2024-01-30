

lado_externo = int(input("Digam un numero per el quadrat extern: "))
lado_interno =int(input("Digam un numero per el quadrat intern: "))

for i in range(lado_externo):
    for j in range(lado_externo):
        if i < lado_interno: # or i >= lado_externo - lado_interno or j < lado_interno or j >= lado_externo - lado_interno:
            print("🌳", end="")
        else:
            print("🔥", end="")
    print()

for i in range(lado_externo):
    for j in range(lado_externo):
        if i < lado_interno or i >= lado_externo - lado_interno: # or j < lado_interno or j >= lado_externo - lado_interno:
            print("🌳", end="")
        else:
            print("🔥", end="")
    print()

for i in range(lado_externo):
    for j in range(lado_externo):
        if i < lado_interno or i >= lado_externo - lado_interno or j < lado_interno: # or j >= lado_externo - lado_interno:
            print("🌳", end="")
        else:
            print("🔥", end="")
    print()

for i in range(lado_externo):
    for j in range(lado_externo):
        if i < lado_interno or i >= lado_externo - lado_interno or j < lado_interno or j >= lado_externo - lado_interno:
            print("🌳", end="")
        else:
            print("🔥", end="")
    print()