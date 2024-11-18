# menu.py

def mostrar_menu():
    print('''
    ☠  ☠  HUB DE INGENIO  ☠  ☠
    1. Trivista
    2. Snake game
    3. Juego de memoria
    4. Calculadora Multiusos.
    5. Salir.
    ''')

def elegir_opcion():
    try:
        opcion = int(input("Seleccione una opción: "))
        return opcion
    except ValueError:
        print("Por favor, ingresa un número válido.")
        return None
