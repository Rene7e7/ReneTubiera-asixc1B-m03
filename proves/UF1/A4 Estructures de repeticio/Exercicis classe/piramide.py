try:
    numero = int(input("Dime numero: "))
    for i in range(0, numero):
        i+=1
        print('🐍 ' * i)
except ValueError:
    print("Error")

