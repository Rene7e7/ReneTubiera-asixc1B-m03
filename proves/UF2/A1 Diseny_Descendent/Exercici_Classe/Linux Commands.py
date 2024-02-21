'''
Al ITB s'està creant un nou sistema operatiu, basat el Linux. De moment, només té unes poques comandes, donat que és una versió alfa.

Les comandes que es poden executar són:

touch

grep

cat

fdisk

cmp

dmesg

man

top

htop

halt   "Cas especial" Aquesta comanda aturarà el sistema, tot i que no l'apagarà

Les opcions que han de tenir implementades per aquesta versió són:

-h, --help

           Mostra un text d'ajuda i surt

 -v, --version

          Mostra la versió i surt

En cas de triar una opció no valida ha de mostrar el missatge: Value xx is not valid option BACALAO"

A on les xx ha de ser l'opció triada que no ha estat valida

Input
fdisk --help

Output
fdisk is a dialog-driven program for creation and manipulation of partition tables.

It understands GPT, MBR, Sun, SGI and BSD partition tables.



Block devices can be divided into one or more logical disks called partitions.

This division is recorded in the partition table, usually found in sector 0 of the disk.

(In the BSD world one talks about `disk slices' and a `disklabel'.)

.  .  .


Input
fdisk -v

Output
v0.1




Input
fdisk -a

Output
Value -a is not valid option, "User BACALAO"


Input
ls -h

Output
ls comand not found, "User BACALAO"


EXTRA:

Com a benvinguda, fer que mostri una frase cada vegada que s'executi l'aplicació.

La frase hauria de ser aleatòria.


CONSELL per a "Cavernícoles"

Más de 400 comandos para GNU/Linux que deberías conocer
'''

llistaComandes= ["touch", "grep", "cat", "fdisk", "cmp", "dmesg", "man", "top", "htop","halt"]
llistaopcions = ["-h", "--help", "-v", "--version"]
Comandas = {
    "fdisk": {
        "-h": "fdisk is a dialog-driven program for creation and manipulation of partition tables. It understands GPT, MBR, Sun, SGI and BSD partition tables. Block devices can be divided into one or more logical disks called partitions. This division is recorded in the partition table, usually found in sector 0 of the disk. (In the BSD world one talks about `disk slices' and a `disklabel'.)",
        "-v": "v0.1",
        "--help": "fdisk is a dialog-driven program for creation and manipulation of partition tables. It understands GPT, MBR, Sun, SGI and BSD partition tables. Block devices can be divided into one or more logical disks called partitions. This division is recorded in the partition table, usually found in sector 0 of the disk. (In the BSD world one talks about `disk slices' and a `disklabel'.)",
        "--version": "v0.1"
    }

}
def comanda():
    while True:
        comanda = input("USER@BACALAOS:~$ ")
        if comanda == "halt":
            break
        else:
            comanda = comanda.split()
            if comprovacioComandesOpcions(comanda[0], comanda[1]):
                execucioComandes(comanda[0], comanda[1])
            else:
                print(f"{comanda[0]} needs one paramater. For instance -v or -h")
                print(f"{comanda[0]} comand not found, User BACALAO")

# comprueba si la comanda y la opción introducida por el usuario son correctas
def comprovacioComandesOpcions(comanda, opcio):
    if comanda in llistaComandes:
        if opcio in llistaopcions:
            return True
        else:
            print(f"Value {opcio} is not valid option, User BACALAO")
            return False
    else:
        return False
# ejecuta la comanda y la opción introducida por el usuario
def execucioComandes(comanda, opcio):
    print(Comandas[comanda][opcio])
comanda()