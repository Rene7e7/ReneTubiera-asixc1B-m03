import leer_archivo
import encontrar_articulo
import escribir_archivo

def main():
    # Nombre del archivo de entrada
    archivo_entrada = 'articulos.txt'

    # Leer la información de los artículos desde el archivo
    datos_articulos = leer_archivo.leer_datos(archivo_entrada)

    if datos_articulos is not None:
        # Clasificar los artículos como caro o barato
        caros, baratos = encontrar_articulo.clasificar_articulos(datos_articulos)

        # Escribir los nombres y precios de los artículos caros en el archivo 'caro.txt'
        escribir_archivo.escribir_articulos('caro.txt', caros)

        # Escribir los nombres y precios de los artículos baratos en el archivo 'barato.txt'
        escribir_archivo.escribir_articulos('barato.txt', baratos)

        print("Proceso completado. Los resultados se han guardado en 'caro.txt' y 'barato.txt'.")

if __name__ == "__main__":
    main()
