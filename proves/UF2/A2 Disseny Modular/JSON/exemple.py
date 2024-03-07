import json

llista_compra = {

    "fruites": ["poma", "pera", "platan", "taronges"],
    "verdures": ["enciams", "espinacs", "pastanaga", "ceba"],
    "llegums": ["llenties", "garrofó", "fesols", "mongetes"]
}
nom_fitxer = "llista_compra.json"

with open("llista_compra.json", "w") as fitxer:
    json.dump(llista_compra, fitxer)

print("llista_compra guardada en llista_compra.json",nom_fitxer)
