from contar_palabras_numeros import contar_palabras, contar_numeros
from leer_archivo import leer_archivo
from escribir_resultados import escribir_resultados

texto = leer_archivo('texto.txt')
if texto:
    frecuencia_palabras = contar_palabras(texto)
    frecuencia_numeros = contar_numeros(texto)

    escribir_resultados('frecuencia_palabras.txt', frecuencia_palabras, 'palabras')
    escribir_resultados('frecuencia_numeros.txt', frecuencia_numeros, 'números')
