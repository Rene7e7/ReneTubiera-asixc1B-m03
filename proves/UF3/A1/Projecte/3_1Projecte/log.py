import os
from datetime import datetime
# Funció per escriure un missatge al fitxer de log
def escriure_log(missatge):
    with open("boges.log", "a") as f:
        f.write(f"{datetime.now()} - {missatge}\n")