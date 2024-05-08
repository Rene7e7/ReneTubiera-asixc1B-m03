class Robot:
    def __init__(self):
        self.posicio = [0.0, 0.0]
        self.velocitat = 1.0

    def moure_dalt(self):
        self.posicio[1] += self.velocitat

    def moure_baix(self):
        self.posicio[1] -= self.velocitat

    def moure_dreta(self):
        self.posicio[0] += self.velocitat

    def moure_esquerra(self):
        self.posicio[0] -= self.velocitat

    def accelerar(self):
        if self.velocitat < 10:
            self.velocitat += 0.5

    def disminuir(self):
        if self.velocitat > 0:
            self.velocitat -= 0.5

    def mostrar_posicio(self):
        print(f"La posició del robot és ({self.posicio[0]}, {self.posicio[1]})")

    def mostrar_velocitat(self):
        print(f"La velocitat del robot és {self.velocitat}")

def moure_robot(ruta_fitxer):
    robot = Robot()

    with open(ruta_fitxer, "r") as f:
        for linia in f:
            accio = linia.strip().upper()
            print(f">{accio}")

            if accio == "DALT":
                robot.moure_dalt()
            elif accio == "BAIX":
                robot.moure_baix()
            elif accio == "DRETA":
                robot.moure_dreta()
            elif accio == "ESQUERRA":
                robot.moure_esquerra()
            elif accio == "ACCELERAR":
                robot.accelerar()
            elif accio == "DISMINUIR":
                robot.disminuir()
            elif accio == "POSICIO":
                robot.mostrar_posicio()
            elif accio == "VELOCITAT":
                robot.mostrar_velocitat()
            elif accio == "END":
                print("Fi del programa")
                break
            else:
                print("Acció no vàlida")
