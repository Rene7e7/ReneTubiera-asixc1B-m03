from contar_vocales_no_vocales import contar_vocales_no_vocales
from leer_archivo import leer_archivo
from escribir_resultados import escribir_resultados

texto = leer_archivo('texto.txt')
if texto:
    frecuencia_vocales, frecuencia_no_vocales = contar_vocales_no_vocales(texto)
    escribir_resultados('vocales.txt', 'no_vocales.txt', frecuencia_vocales, frecuencia_no_vocales)
