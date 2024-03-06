import os


def menu():

    opts = ['1', '2', '3', '4', '5']

    msg = """

    Elija una opción:

    1. Pesos a Dolares
    2. Pesos a Euros
    3. Euros a Pesos
    4. Pesos a Yenes
    5. Salir

    """
    print(msg)
    opt = input('Ingrese una opción:\n-> ')
    if opt not in opts:
        print('La opción no es valida')
        os.system('pause')
        menu()
    else:

        if opt == '1':
            pesos_dolares()
            menu()
        elif opt == '2':
            pesos_euros()
            menu()
        elif opt == '3':
            pesos_euros()
            menu()
        elif opt == '4':
            pesos_yenes()
            menu()
        elif opt == '5':
            return
            


dolar = 3944

def pesos_dolares():

    try:
        pesos = float(input('Ingrese la cantidad de pesos a convertir a dolares:\n-> '))
    except ValueError:
        print('El dato debe ser de tipo flotante')
        os.system('pause')
        pesos_dolares()
    else:

        peso = 1 / dolar

        result = pesos * peso
        print(f'{pesos} pesos son igual a {round(result, 3)} dolares')
        os.system('pause')
        return
    


euro = 4279

def pesos_euros():

    try:
        pesos = float(input('Ingrese la cantidad de pesos a convertir a euros:\n-> '))
    except ValueError:
        print('El dato debe ser de tipo flotante')
        os.system('pause')
        pesos_dolares()
    else:

        peso = 1 / euro

        result = pesos * peso
        print(f'{pesos} pesos son igual a {round(result, 3)} euros')
        os.system('pause')
        return


yen = 26.30

def pesos_yenes():

    try:
        pesos = float(input('Ingrese la cantidad de pesos a convertir a yenes:\n-> '))
    except ValueError:
        print('El dato debe ser de tipo flotante')
        os.system('pause')
        pesos_dolares()
    else:

        peso = 1 / yen

        result = pesos * peso
        print(f'{pesos} pesos son igual a {round(result, 3)} yenes')
        os.system('pause')
        return