from modules.corefiles import read_file, update_file, clear_screen, pause_screen
from modules.empleado_module import add_empleado, add_sueldo_empleado, reg_col_empl, lst_col_empl

def menu():

    opts = ['1', '2', '3', '4', '5', '6']

    msg = """

    Elija una opción:

    1. Registrar Empleados
    2. Calcular Salario
    3. Registrar Colilla
    4. Total Nomina
    5. Consultar Colilla
    6. Salir

    """
    print(msg)
    opt = input('Ingrese una opción:\n-> ')
    if opt not in opts:
        print('La opción no es valida')
        pause_screen()
        menu()
    else:

        if opt == '1':
            add_empleado()
            menu()
        elif opt == '2':
            add_sueldo_empleado()
            menu()
        elif opt == '3':
            reg_col_empl()
            menu()
        elif opt == '4':
            lst_col_empl()
            menu()
        elif opt == '5':
            menu()
        elif opt == '6':
            return
