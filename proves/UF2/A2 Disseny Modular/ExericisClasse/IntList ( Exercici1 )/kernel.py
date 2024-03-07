'''
Rene Tubiera
'''

def readIntListFromKeyboard():
    try:
        numbers = []
        number = input()
        for i in number.split():
            if i == "-1":
                break
            numbers.append(int(i))
        return numbers
    except ValueError:
        print("Error: Invalid input")





