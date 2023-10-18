"""
Rene Tubiera Sadinas
Exercici 15
Escriu el programa que demani a l'usuari el valor de dues variables variableA i variableB .
Ha d’intercanviar els seus valors. És a dir, el contingut de la variableA ha d’estar en la
variableB, i el de la variableB a la variableA. Finalment els ha de mostrar per pantalla

"""
# Crear 2 variables A i B
VariableA = int(input("Dime un valor para VariableA: "))
VariableB = int(input("Dime un valor para VariableB: "))

VariableAM = str(VariableA)
VariableBM = str(VariableB)

VariableB_Remplazo = VariableAM.replace(VariableBM, VariableAM)
VariableA_Remplazo = VariableBM.replace(VariableAM, VariableBM)

print("VariableA después de reemplazar:", VariableA_Remplazo)
print("VariableB después de reemplazar:", VariableB_Remplazo)






