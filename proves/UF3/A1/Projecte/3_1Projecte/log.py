import os

def escriure_log(missatge):
    with open("boges.log", "a") as f:
        f.write(missatge + "\n")
