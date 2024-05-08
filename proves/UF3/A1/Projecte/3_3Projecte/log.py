import os
from datetime import datetime

def escriure_log(missatge):
    with open("boges.log", "a") as f:
        f.write(f"{datetime.now()} - {missatge}\n")