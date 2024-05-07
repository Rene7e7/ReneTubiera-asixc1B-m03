with open('3_3Projecte/entrada/paraules.txt', 'w') as f:
    for i in range(20000):
        f.write("Esta es la línea número " + str(i+1) + "\n")
