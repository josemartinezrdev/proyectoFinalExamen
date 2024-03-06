import os, sys, json


# VARIABLES PARA EL JSON

BASE = 'data/'

# FUNCIONES DE PANTALLA

def clear_screen():
    if sys.platform == "linux" or sys.platform == "darwin":
        os.system("clear")
    else:
        os.system("cls")


def pause_screen():
    if sys.platform == "linux" or sys.platform == "darwin":
        x = input("Presione una tecla para continuar...")
    else:
        os.system("pause")


#FUNCIONES PARA EL JSON

def check_file(archivo: str, data):
    if (not (os.path.isfile(BASE + archivo))):
        with open(BASE + archivo, "w") as bw:
            json.dump(data, bw, indent=4)


def read_file(archivo: str):
    with open(BASE+archivo, 'r') as rf:
        inventario = json.load(rf)
    return inventario


def update_file(archivo, data):
    with open(BASE + archivo, 'w') as fw:
        json.dump(data, fw, indent=4)
