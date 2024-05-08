import funciones_registro_eventos as fre

def main():
    evento = input("Introduce el evento: ")
    fre.registrar_evento(evento)
    print("Evento registrado correctamente.")

if __name__ == "__main__":
    main()
