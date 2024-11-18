# main.py

import menu  # Importa las funciones del menú
import TPIcompleto  # Importa las funciones de los juegos

def ejecutar_programa():
    opcion = 0
    while opcion != 5:
        menu.mostrar_menu()  # Muestra el menú
        opcion = menu.elegir_opcion()  # Pide la opción al usuario

        if opcion == 1:
            print("Opción Trivista seleccionada. (Aquí va tu código para el juego Trivista)")
        elif opcion == 2:
            TPIcompleto.jugar_snake_game()  # Llama a la función para jugar el juego de la serpiente
        elif opcion == 3:
            TPIcompleto.juego_memoria()
        elif opcion == 4:
            TPIcompleto.calculadora()
        elif opcion == 5:
            print("Saliendo del programa...")
        else:
            print("Opción inválida. Por favor, ingresa una opción válida.")

if __name__ == "__main__":
    ejecutar_programa()
