from modules.corefiles import read_file, update_file
import os

def menu():
    os.system('cls')

    opts = ['1', '2']

    msg = """

    Elija una opción:

    1. Registrar usuario
    2. Salir

    """
    print(msg)
    opt = input('Ingrese una opción:\n-> ')
    if opt not in opts:
        print('La opción no es valida')
        os.system('pause')
        menu()
    else:

        if opt == '1':
            add_user()
            menu()
        elif opt == '2':
            return
        
def add_user():
    inventario = read_file('inventario.json')

    idx = input('Ingrese el id del producto:\n-> ')
    os.system('cls')
    nombre = input('Ingrese el nombre del producto:\n-> ')
    os.system('cls')

    def nums():
        os.system('cls')

        try:
            valor_unitario = float(input(f'Ingrese el valor unitario de el/la {nombre}:\n-> '))
            os.system('cls')
            stock_min = float(input(f'Ingrese el stock minimo de el/la {nombre}:\n-> '))
            os.system('cls')
            stock_max = float(input(f'Ingrese el stock maximo de el/la {nombre}:\n-> '))
            os.system('cls')
        except ValueError:
            print('Los datos deben ser de tipo flotantes')
            os.system('pause')
            nums()
        else:
            return valor_unitario, stock_min, stock_max
        
        
    valor_unitario, stock_min, stock_max = nums()
    os.system('cls')

    producto = {
        'idx': idx,
        'nombre': nombre,
        'valor_unitario': valor_unitario,
        'stock_min': stock_min,
        'stock_max': stock_max
    }

    inventario.update({idx:producto})
    update_file('inventario.json', inventario)