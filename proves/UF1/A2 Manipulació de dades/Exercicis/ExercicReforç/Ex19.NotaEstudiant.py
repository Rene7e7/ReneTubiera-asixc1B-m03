"""
Exercici 19
Implementa el programa que calculi la nota d'un test dut a terme per un estudiant.

La nota es calcularà així: per cada resposta correcta se sumaran cinc punts, per cada
incorrecta es restarà un punt i les respostes en blanc ni sumaran ni restaran. El programa
demanarà les dades estrictament necessàries i mostrarà en pantalla la nota del test.

"""
preguntas_erroneas = 0
preguntes_correctes = 0

pregunta1 = input("Qual es la capital de Francia?: ")
if pregunta1 == "Paris":
    preguntes_correctes += 5
else:
    preguntas_erroneas += 1

pregunta1 = input("Qual es la capital de Mexico?: ")
if pregunta1 == "Mexico":
    preguntes_correctes += 5
else:
    preguntas_erroneas += 1

pregunta1 = input("Qual es la capital de Filipinas?: ")
if pregunta1 == "Manila":
    preguntes_correctes += 5
else:
    preguntas_erroneas += 1

pregunta1 = input("Qual es la capital de España?: ")
if pregunta1 == "Madrid":
    preguntes_correctes += 5
else:
    preguntas_erroneas += 1

print("preguntes correctes: ", preguntes_correctes)
print("preguntes erroneas: ", preguntas_erroneas)
print("Nota del test:", preguntes_correctes - preguntas_erroneas)
print("Nota sobre 10: ", (preguntes_correctes/20)*10)




