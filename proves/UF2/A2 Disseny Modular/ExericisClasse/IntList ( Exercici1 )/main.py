'''
Rene Tubiera
UF2 A2 Disseny modulars
'''

from kernel import readIntListFromKeyboard


def main():
    print("Introdueix una llista de numeros enters separats per espais. Per acabar introdueix -1")
    numbers = readIntListFromKeyboard()
    print(numbers)
main()
