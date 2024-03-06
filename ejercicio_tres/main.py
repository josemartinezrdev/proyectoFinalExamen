from modules.corefiles import check_file
from modules.funcs import menu

if __name__ == '__main__':

    inventario = {}

    check_file('inventario.json', inventario)
    menu()