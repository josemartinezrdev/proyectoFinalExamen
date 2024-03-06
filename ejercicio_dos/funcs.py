import os

users = {}

def menu():
    os.system('cls')

    opts = ['1', '2', '3']

    msg = """

    Elija una opción:

    1. Registrar usuario
    2. Ver usuario
    3. Salir

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
            list_user()
            menu()
        elif opt == '3':
            return


def add_user():
    os.system('cls')

    idx = input('Ingrese el id del usuario:\n-> ')
    os.system('cls')
    nombre = input('Ingrese los nombre del usuario:\n-> ')
    os.system('cls')
    apellidos = input(f'Ingrese los apellidos de {nombre}\n-> ')
    os.system('cls')
    direccion = input(f'Ingrese la dirección de {nombre}\n-> ')
    os.system('cls')
    ciudad = input(f'Ingrese la ciudad de {nombre}\n-> ')
    os.system('cls')
    long = input(f'Ingrese la longitud\n-> ')
    os.system('cls')
    lat = input(f'Ingrese la latitud\n-> ')
    os.system('cls')
    email = input(f'Ingrese el email de {nombre}\n-> ')
    os.system('cls')
    edad = input(f'Ingrese la edad de {nombre}\n-> ')
    os.system('cls')
    ocupacion = input(f'Ingrese la ocupacion de {nombre}\n-> ')
    os.system('cls')

    usuario = {
        'idx': idx,
        'nombre': nombre,
        'apellidos': apellidos,
        'ubicacion': {
            'direccion': direccion,
            'ciudad': ciudad,
            'long': long,
            'lat': lat,
        },
        'email': email,
        'edad': edad,
        'ocupacion': ocupacion
    }

    users.update({idx:usuario})
    return

def list_user():

    if len(users) == 0:
        print('Aun no hay usuarios registrados')
        os.system('pause')
    else:
        os.system('cls')
        print(users)
        os.system('pause')
        os.system('cls')
        return

