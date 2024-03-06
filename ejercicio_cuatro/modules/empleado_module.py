from modules.corefiles import clear_screen, pause_screen, read_file, update_file


# empresa {
#     idEmpl {
#         dato: dato
#         dato: dato
#         dato: dato
#         dato: dato
#         salario: salario
#         colilla {
#             mesPagado: mesPagado
#             datos: datos
#             datos: datos
#             datos: datos
#             datos: datos
#         }
#     }
# }


def add_empleado():
    clear_screen()

    empresa = read_file('empresa.json')

    idx = input('Ingrese el id del empleado que va a registrar:\n-> ')
    clear_screen()
    nombre = input('Ingrese el nombre del empleado:\n-> ')
    clear_screen()

    cargo = ing_cargo()
    clear_screen()

    sal = True
    while sal:
        try:
            clear_screen()
            salario = int(input('Ingrese el salario base del empleado:\n-> '))
            if salario <= 0:
                sal = True
        except ValueError:
            print('Los datos deben ser de tipo flotante')
            pause_screen()
            sal = True
            clear_screen()
        else:
            clear_screen()
            sal = False

    empleado = {
        'idx': idx,
        'nombre': nombre,
        'cargo': cargo,
        'salario_base': salario,
        'deuda_empresa': 0,
        'deuda_cafeteria': 0,
        'salario_final': 0,
        'colilla': {}
    }

    empresa.update({idx: empleado})
    update_file('empresa.json', empresa)

# FUNCIONES ADD_EMPLEADO


def ing_cargo():
    clear_screen()
    cargos = ['1', '2', '3', '4', '5']
    msg_cargos = """
        Elija el número del cargo:

        1. Almacenista
        2. Jefe IT
        3. Administrador
        4. Mensajero
        5. Gerente
    """
    print(msg_cargos)
    cargo = input('\n-> ')
    if cargo not in cargos:
        print('El cargo no es valido')
        pause_screen()
        ing_cargo()
    else:
        if cargo == '1':
            cargo = 'Almacenista'
        elif cargo == '2':
            cargo = 'Jefe IT'
        elif cargo == '3':
            cargo = 'Administrador'
        elif cargo == '4':
            cargo = 'Mensajero'
        elif cargo == '4':
            cargo = 'Gerente'

    return cargo


def add_sueldo_empleado():

    empresa = read_file('empresa.json')

    emp = input(
        'Ingrese el id del empleado al que le va a añadir el sueldo:\n-> ')
    if emp not in empresa:
        print('El empleado no esta en la empresa')
    else:

        sueldo_final = 0

        sueldo_base = empresa[emp]['salario_base']
        sueldo_diario = sueldo_base / 30

        dias_trab = int(input('Ingrese los dias trabajados:\n-> '))
        sueldo_final += (dias_trab * sueldo_diario)

        horas_ex = int(
            input('Ingrese las horas extras, si no tiene ingrese 0:\n-> '))
        precio_ex = 5500
        sueldo_final += (horas_ex * precio_ex)

        deuda_cafeteria = int(
            input('Ingrese la deuda con la cafeteria, si no tiene ingrese 0:\n-> '))
        sueldo_final -= deuda_cafeteria

        deuda_empresa = int(
            input('Ingrese la deuda con la empresa, si no tiene ingrese 0:\n-> '))
        sueldo_final -= deuda_empresa

        empresa[emp]['salario_final'] = sueldo_final
        update_file('empresa.json', empresa)


def reg_col_empl():

    empresa = read_file('empresa.json')

    emp = input('Ingrese el id del empleado al que le va a añadir el sueldo:\n-> ')
    if emp not in empresa:
        print('El empleado no esta en la empresa')
    else:

        mes = input('Ingrese el mes en el que se hace el pago:\n-> ')
        fecha = input('Ingrese la fecha en la que se hace el pago:\n-> ')
        sueldo_base = empresa[emp]['salario_base']
        precio_ex = 5000
        deuda_empresa = empresa[emp]['deuda_empresa']
        deuda_cafeteria = empresa[emp]['deuda_cafeteria']
        total_pagar = empresa[emp]['salario_final']

        col = {

            'mes': mes,
            'fecha': fecha,
            'sueldo_base': sueldo_base,
            'precio_ex': precio_ex,
            'deuda_empresa': deuda_empresa,
            'deuda_cafeteria': deuda_cafeteria,
            'total_pagar': total_pagar

        }

        empresa[emp]['colilla'].update({mes:col})
        update_file('empresa.json', empresa)

def lst_col_empl():
    pass
