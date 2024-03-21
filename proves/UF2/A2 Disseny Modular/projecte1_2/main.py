# Aquí van els imports i les definicions de funcions del codi que has compartit
from crazy_words import dividir, identificar_paraules, identificar_caracters_especials, aleatorizar_parte_medio, juntar_llista, LISTA
from data_source import get_data_from_keyboard, get_data_from_chatgpt
def main():
    # Aquí va el codi de l'exercici anterior fins just abans de processar les dades

    # En lloc de processar les dades directament, crida a les funcions del codi que has compartit
    oracio = get_data_from_keyboard()
    paraules = dividir(oracio)
    paraules_desordenades = identificar_paraules(paraules)
    paraules_aleatoritzades = [aleatorizar_parte_medio(paraula) if paraula in paraules_desordenades else paraula for paraula in paraules]
    juntar_llista(paraules_aleatoritzades)

    # Aquí va la resta del codi de l'exercici anterior
    # crida la funcio de get_data_from_chatgpt


if __name__ == "__main__":
    main()
    get_data_from_chatgpt()



