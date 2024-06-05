from leer_archivo import leer_archivo
from procesar_notas import procesar_notas
from escribir_resultados import escribir_resultados

# Cambia 'notas.txt' por el nombre de tu archivo de entrada
lista_notas = leer_archivo('notas.txt')
if lista_notas is not None:
    aprobados, suspendidos = procesar_notas(lista_notas)
    # Cambia 'aprobados.txt' y 'suspendidos.txt' por los nombres de tus archivos de salida
    escribir_resultados('aprobados.txt', aprobados, 'Aprobado')
    # Cambia 'aprobados.txt' y 'suspendidos.txt' por los nombres de tus archivos de salida
    escribir_resultados('suspendidos.txt', suspendidos, 'Suspendido')
