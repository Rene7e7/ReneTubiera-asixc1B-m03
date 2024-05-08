def calcular_marcador(historial):
    punts_a = 0
    punts_b = 0
    set_a = 0
    set_b = 0
    marcador = ""

    for punt in historial:
        if punt == "A":
            punts_a += 1
        elif punt == "B":
            punts_b += 1
        elif punt == "F":
            if set_a >= 3 or set_b >= 3:
                if set_a > set_b:
                    marcador += f"{punts_a}-{punts_b} "
                else:
                    marcador += f"{punts_a}-{punts_b} "
                return marcador.strip()
            else:
                marcador += f"{punts_a}-{punts_b} "
                punts_a = 0
                punts_b = 0
                set_a += 1
        if punts_a >= 9 and punts_a - punts_b >= 2:
            set_a += 1
            punts_a = 0
            punts_b = 0
        elif punts_b >= 9 and punts_b - punts_a >= 2:
            set_b += 1
            punts_a = 0
            punts_b = 0
        elif punts_a == 10 and punts_b == 8:
            set_a += 1
            punts_a = 0
            punts_b = 0
        elif punts_b == 10 and punts_a == 8:
            set_b += 1
            punts_a = 0
            punts_b = 0
        elif punts_a == 11 and punts_b == 9:
            set_a += 1
            punts_a = 0
            punts_b = 0
        elif punts_b == 11 and punts_a == 9:
            set_b += 1
            punts_a = 0
            punts_b = 0

    return marcador.strip()
