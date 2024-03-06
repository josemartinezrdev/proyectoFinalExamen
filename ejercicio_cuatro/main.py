from modules.corefiles import check_file, clear_screen, pause_screen
from modules.menu import menu

empresa = {}

check_file('empresa.json', empresa)

menu()