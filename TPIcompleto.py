import pygame, sys, random, Font, time #INSTALA DRIVERS Q HACEN POSIBLE EL JUEGO
def programa_principal():
    # definan el juego completo como funcion y copien y peguenlo aca, falta el trivista y el master, tengan en cuenta de que
    #los juegos tienen que tener una opcion  para volver a este menu.
    # acuerdense de llamar a la funcion abajo en el menu
    #el ultimo que edite esto borre estas aclaraciones
    
    def programa_1():
        print()
        # Ingresen el trivisita

import pygame
import random
import sys

def programa_2():
    pygame.init()

    # Definir el tamaño de la pantalla y los FPS
    play_surface = pygame.display.set_mode((500, 500))
    fps = pygame.time.Clock()

    # Definir el tipo de letra dentro de la función
    fuente_letra = pygame.font.Font(None, 30)

    # Colores de la serpiente
    colores = {
        1: (255, 0, 0),    # ROJO
        2: (0, 255, 0),    # VERDE
        3: (0, 255, 255),  # CELESTE
        4: (0, 0, 255),    # AZUL
        5: (128, 0, 128)   # VIOLETA
    }

    def pedir_nombre_y_color(jugador_num):
        print(f"\nJugador {jugador_num}:")
        nombre = input("Ingresa el nombre de la serpiente: ")
        print("Elige el color de la serpiente:")
        print("1. Rojo")
        print("2. Verde")
        print("3. Celeste")
        print("4. Azul")
        print("5. Violeta")
        
        color_opcion = None
        while color_opcion not in colores:
            try:
                color_opcion = int(input("Ingresa el número del color elegido (1-5): "))
                if color_opcion not in colores:
                    print("Número ingresado incorrecto. Por favor elige un número entre 1 y 5.")
            except ValueError:
                print("Entrada inválida. Por favor ingresa un número.")
        
        color = colores[color_opcion]
        return f"Jugador {jugador_num} - {nombre}", color

    def comida():
        random_pos = random.randint(0, 49) * 10
        comida_pos = [random_pos, random_pos]
        return comida_pos

    def guardar_puntuaciones(jugadores):
        mayor_puntaje = max(jugadores, key=lambda x: x[1])
        with open("puntuaciones.txt", "w") as archivo:
            archivo.write(f"¡¡GANADOR CON MAXIMA PUNTUACION:!! {mayor_puntaje[0]} - {mayor_puntaje[1]}\n")
            for jugador, puntaje in jugadores:
                archivo.write(f"{jugador}: {puntaje}\n")

    def main():
        jugadores = []
        for i in range(1, 4):  # Itera los jugadores 1, 2 y 3
            nombre, color = pedir_nombre_y_color(i)
            jugadores.append((nombre, color))

        resultados = []  # Guarda el puntaje de cada jugador

        for nombre, color in jugadores:
            snake_cabeza = [100, 50]
            snake_cuerpo = [[100, 50], [90, 50], [80, 50]]
            sentido = "RIGHT"
            run = True
            comida_pos = comida()
            puntaje = 0
            max_puntuacion = 0

            while run:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RIGHT:
                            sentido = "RIGHT"
                        if event.key == pygame.K_LEFT:
                            sentido = "LEFT"
                        if event.key == pygame.K_UP:
                            sentido = "UP"
                        if event.key == pygame.K_DOWN:
                            sentido = "DOWN"

                if sentido == "RIGHT":
                    snake_cabeza[0] += 10
                if sentido == "LEFT":
                    snake_cabeza[0] -= 10
                if sentido == "UP":
                    snake_cabeza[1] -= 10
                if sentido == "DOWN":
                    snake_cabeza[1] += 10

                snake_cuerpo.insert(0, list(snake_cabeza))
                
                if snake_cabeza == comida_pos:
                    comida_pos = comida()
                    puntaje += 1
                    max_puntuacion = max(max_puntuacion, puntaje)
                else:
                    snake_cuerpo.pop()

                play_surface.fill((0, 0, 0))  # Pantalla negra
                for cabeza in snake_cuerpo:
                    pygame.draw.rect(play_surface, color, pygame.Rect(cabeza[0], cabeza[1], 10, 10))

                texto = fuente_letra.render(f"Puntaje: {puntaje}", 0, (255, 0, 255))
                play_surface.blit(texto, (380, 20))
                
                texto_max = fuente_letra.render(f"Max: {max_puntuacion}", 0, (255, 255, 0))
                play_surface.blit(texto_max, (10, 20))
                
                texto_nombre = fuente_letra.render(f"Jugador: {nombre}", 0, (255, 255, 255))
                play_surface.blit(texto_nombre, (10, 50))

                if puntaje < 5:
                    fps.tick(10)
                elif puntaje < 10:
                    fps.tick(15)
                else:
                    fps.tick(20)

                if snake_cabeza[0] < 0 or snake_cabeza[0] >= 500 or snake_cabeza[1] < 0 or snake_cabeza[1] >= 500:
                    run = False
                    print("PERDISTE")

                pygame.draw.rect(play_surface, (169, 6, 6), pygame.Rect(comida_pos[0], comida_pos[1], 9, 9))
                pygame.display.flip()

            resultados.append((nombre, puntaje))

        guardar_puntuaciones(resultados)

    main()

# Llamamos a la función principal
programa_2()

        #ingresen el juego de master

def juego_memoria():

        import random
        import time

        # Nombre del archivo para guardar el puntaje máximo
        ARCHIVO_PUNTAJE = "puntaje_maximo.txt"

        # Función para cargar el puntaje máximo desde el archivo
        def cargar_puntaje_maximo():
            try:
                with open(ARCHIVO_PUNTAJE, "r") as archivo:
                    return int(archivo.read())
            except (FileNotFoundError, ValueError):
                return 0

        # Función para guardar el puntaje máximo en el archivo
        def guardar_puntaje_maximo(puntaje):
            with open(ARCHIVO_PUNTAJE, "w") as archivo:
                archivo.write(str(puntaje))

        # Lógica principal del juego de memoria
        while True:
            print("\n--- Juego de Memoria ---")
            print("1. Jugar")
            print("2. Volver al Hub de Ingenio")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                puntaje_maximo = cargar_puntaje_maximo()
                secuencia = []
                puntaje = 0

                print("¡Bienvenido al juego de memoria!")
                print(f"Puntaje máximo actual: {puntaje_maximo}")
                print("Recuerda la secuencia y escríbela correctamente.")

                while True:
                    # Agregar un nuevo número a la secuencia
                    secuencia.append(random.randint(0, 9))
                    
                    # Mostrar la secuencia al usuario
                    print("\nSecuencia:")
                    for numero in secuencia:
                        print(numero, end=" ", flush=True)
                        time.sleep(0.5)
                    print("\n" + "-" * 20)
                    
                    # Limpiar la pantalla (opcional)
                    print("\033[H\033[J")  # Esto limpia la pantalla en terminales compatibles

                    # Pedir al usuario que ingrese la secuencia
                    respuesta = input("Ingresa la secuencia: ").split()

                    # Convertir la respuesta a una lista de enteros
                    try:
                        respuesta = [int(x) for x in respuesta]
                    except ValueError:
                        print("Entrada inválida. Fin del juego.")
                        break

                    # Verificar si la respuesta es correcta
                    if respuesta == secuencia:
                        puntaje += 1
                        print(f"¡Correcto! Puntaje actual: {puntaje}")
                    else:
                        print("Respuesta incorrecta. Fin del juego.")
                        break

                # Mostrar el puntaje final
                print(f"Puntaje final: {puntaje}")

                # Verificar si se ha alcanzado un nuevo puntaje máximo
                if puntaje > puntaje_maximo:
                    print("¡Nuevo puntaje máximo!")
                    guardar_puntaje_maximo(puntaje)

            elif opcion == "2":
                print("Regresando al Hub de Ingenio...")
                break
            else:
                print("Opción inválida. Intente nuevamente.")


def calculadora():
    # FUNCIONES DE LAS OPERACIONES BASICAS
        def suma(a, b):
            return a + b

        def resta(a, b):
            return a - b

        def multiplicacion(a, b):
            return a * b

        def division(a, b):
            if b != 0:
                return a / b
            else:
                return "Error: División por cero."

        def raiz(indice, radicando):  # primer parámetro índice, segundo parámetro radicando (índice √ radicando)
            if radicando < 0 and indice % 2 == 0:
                return "Error: No se puede calcular la raíz de un número negativo con un índice par"
            return radicando ** (1 / indice)

        def potencia(a, b):
            return a ** b

        # FUNCIONES DE LAS CONVERSIONES DE UNIDADES
        def convertir_libras_a_kilogramos(valor, tipo_conversion):
            if tipo_conversion == 1:  # Libras a kilogramos
                return valor * 0.453592
            elif tipo_conversion == 2:  # Kilogramos a libras
                return valor / 0.453592
            else:
                return "Opción de conversión inválida"

        def convertir_pulgadas_a_centimetros(valor, tipo_conversion):
            if tipo_conversion == 1:  # Pulgadas a centímetros
                return valor * 2.54
            elif tipo_conversion == 2:  # Centímetros a pulgadas
                return valor / 2.54
            else:
                return "Opción de conversión inválida"

        def convertir_pies_a_metros(valor, tipo_conversion):
            if tipo_conversion == 1:  # Pies a metros
                return valor * 0.3048
            elif tipo_conversion == 2:  # Metros a pies
                return valor / 0.3048
            else:
                return "Opción de conversión inválida"

        def convertir_millas_a_kilometros(valor, tipo_conversion):
            if tipo_conversion == 1:  # Millas a kilómetros
                return valor * 1.60934
            elif tipo_conversion == 2:  # Kilómetros a millas
                return valor / 1.60934
            else:
                return "Opción de conversión inválida"

        def convertir_fahrenheit_a_celsius(valor, tipo_conversion):
            if tipo_conversion == 1:  # Fahrenheit a Celsius
                return (valor - 32) * 5 / 9
            elif tipo_conversion == 2:  # Celsius a Fahrenheit
                return (valor * 9 / 5) + 32
            else:
                return "Opción de conversión inválida"

        # FUNCIÓN LINEAL
        def calcular_ecuacion_lineal(X1, Y1, X2, Y2):
            if X2 == X1:
                print("Error: Las coordenadas X no pueden ser iguales. La recta es vertical.")
                return
            m = (Y2 - Y1) / (X2 - X1)
            b = Y1 - m * X1
            if b >= 0:
                print(f"La ecuación de la recta es: y = {m}x + {b}")
            else:
                print(f"La ecuación de la recta es: y = {m}x - {-b}")

        # MENÚ PRINCIPAL DE LA CALCULADORA
        opcion_principal = 0
        while opcion_principal != 4:
            print('''CALCULADORA MULTIUSOS
            1. Operaciones básicas.
            2. Conversor de unidades.
            3. Calculadora de función lineal.
            4. Salir.''')
            opcion_principal = int(input("Seleccione una opción: "))

            if opcion_principal == 1:
                
                opcion = 0
                while opcion != 7:

                    print('''Elija la operación que desea realizar: 
            1. Suma.
            2. Resta.
            3. Multiplicación.
            4. División.
            5. Radicación.
            6. Potenciación.
            7. Volver al menú principal.''')

                    opcion = int(input("Ingrese número de la opción: "))
                    if opcion == 1:
                        num1 = float(input("Ingrese el primer número: "))
                        num2 = float(input("Ingrese el segundo número: "))
                        print(suma(num1, num2))
                    elif opcion == 2:
                        num1 = float(input("Ingrese el primer número: "))
                        num2 = float(input("Ingrese el segundo número: "))
                        print(resta(num1, num2))
                    elif opcion == 3:
                        num1 = float(input("Ingrese el primer número: "))
                        num2 = float(input("Ingrese el segundo número: "))
                        print(multiplicacion(num1, num2))
                    elif opcion == 4:
                        num1 = float(input("Ingrese el primer número: "))
                        num2 = float(input("Ingrese el segundo número: "))
                        print(division(num1, num2))
                    elif opcion == 5:
                        indice = int(input("Ingrese el índice de la raíz: "))
                        radicando = float(input("Ingrese el radicando: "))
                        print(raiz(indice, radicando))
                    elif opcion == 6:
                        num1 = float(input("Ingrese la base: "))
                        num2 = float(input("Ingrese el exponente: "))
                        print(potencia(num1, num2))
                    elif opcion == 7:
                        print("Volviendo al menú principal...")
                    else:
                        print("Opción inválida.")
            elif opcion_principal == 2:
                    opcion_conversor = 0

                    while opcion_conversor != 6:

                        print("""Eliga la conversion que quiera realizar:
            1. Libras a kilogramos o kilogramos a libra
            2. Pulgadas a centimetros o centimetros a pulgadas
            3. Pies a metros o metros a pies
            4. Millas a kilometros o kilometros a millas
            5. Fahrenheit a celsius o de celsius a farenheit
            6. Volver al menu principal de la calculadora""")
                    
                        opcion_conversor = int(input("Ingrese numero de la opcion: "))
                        if opcion_conversor == 6:
                            print("Menú principal de la calculadora.")
                        if opcion_conversor == 1:
                                nume1 = int(input("Ingrese el tipo de conversion 1: de lb a Kg o 2 de Kg a Lb "))
                                nume2 = float(input("El valor a convertir "))
                                print(convertir_libras_a_kilogramos(nume2,nume1))
                        elif opcion_conversor == 2:
                                nume1 = int(input("Ingrese el tipo de conversion: 1: de In a cm 2 de Cm a In "))
                                nume2 = float(input("El valor a convertir "))
                                print(convertir_pulgadas_a_centimetros(nume2,nume1))
                        elif opcion_conversor == 3:
                                nume1 = int(input("Ingrese el tipo de conversion: 1: de ft a M o 2 de M a Ft "))
                                nume2 = float(input("El valor a convertir "))
                                print(convertir_pies_a_metros(nume2,nume1))
                        elif opcion_conversor == 4:
                                nume1 = int(input("Ingrese el tipo de conversion: 1: Mi a KM 2: Km a Mi "))
                                nume2 = float(input("El valor a convertir "))
                                print(convertir_millas_a_kilometros(nume2,nume1)) 
                        elif opcion_conversor == 5:
                                nume1 = int(input("Ingrese el tipo de conversion: 1: ªf a ªC 2:ªC a ªF "))
                                nume2 = float(input("El valor a convertir "))
                                print(convertir_fahrenheit_a_celsius(nume2,nume1))                       
                        else:
                            print("Opcion invalida")
            elif opcion_principal == 3:
                x1 = float(input("Ingrese el valor de X1: "))
                y1 = float(input("Ingrese el valor de Y1: "))
                x2 = float(input("Ingrese el valor de X2: "))
                y2 = float(input("Ingrese el valor de Y2: "))
                calcular_ecuacion_lineal(x1, y1, x2, y2)
            elif opcion_principal == 4:
                print("Saliendo de la calculadora.")
            else:
                print("Opción inválida.")


   

opcion_principal = 0

while opcion_principal != 5:  
        print('''
        ☠  ☠  HUB DE INGENIO  ☠  ☠
        1. Trivista
        2. Snake game
        3. juego de memoria
        4. Calculadora Multiusos.
        5. Salir.
        ''')
        try:
            opcion_principal = int(input("Seleccione una opción: "))
            
            # if opcion_principal == 1:
                # programa_1()
            if opcion_principal == 2:
                programa_2() 
            elif opcion_principal == 3:
                juego_memoria()
            elif opcion_principal == 4:
                calculadora()
            elif opcion_principal == 5:
                print("Saliendo del programa...")
            else:
                print("Opción inválida. Intente de nuevo.")
        except ValueError:
            print("Error: Por favor ingrese un número válido.")


programa_principal()