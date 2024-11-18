def programa_principal():
   
    def programa_1():
         print("Iniciando Trivista")
        
    PreguntasTrivia = {
        "Biologia": [
            {"pregunta": "¿Cual es el tipo de celula que no tiene nucleo?", "respuesta": "procariota"},
            {"pregunta": "¿Cual es la molecula que almacena la informacion genetica?", "respuesta": "adn"},
            {"pregunta": "¿Como se llama el proceso por el cual las plantas producen su alimento?", "respuesta": "fotosintesis"},
            {"pregunta": "¿Cual es el hueso mas largo del cuerpo humano?", "respuesta": "femur"},
            {"pregunta": "¿Cual es el mamifero que puede volar?", "respuesta": "murcielago"},
            {"pregunta": "¿Cual es el depredador mas grande de la tierra?", "respuesta": "orca"},
        ],
        "Arte": [
            {"pregunta": "¿Quién es conocido como: El rey del rock?", "respuesta": "elvis"},
            {"pregunta": "¿Qué compositor es conocido por su Quinta sinfonía?", "respuesta": "beethoven"},
            {"pregunta": "¿Quién pintó el cuadro: Las Meninas?", "respuesta": "velazquez"},
            {"pregunta": "¿En qué película aparece el personaje de Vito Corleone?", "respuesta": "el padrino"},
            {"pregunta": "¿Quién pintó el techo de la Capilla Sixtina?", "respuesta": "miguel angel"},
            {"pregunta": "¿Quién pintó el cuadro: El grito?", "respuesta": "munch"}
        ],
        "Geografía": [
            {"pregunta": "¿Cuál es el país más grande del mundo?", "respuesta": "rusia"},
            {"pregunta": "¿En qué continente se encuentra Egipto?", "respuesta": "africa"},
            {"pregunta": "¿Cuál es la capital de Japón?", "respuesta": "tokio"},
            {"pregunta": "¿Cuál es la capital de Canadá?", "respuesta": "ottawa"},
            {"pregunta": "¿Qué país tiene las cataratas del Niágara?", "respuesta": "canada"},
            {"pregunta": "¿Qué país es conocido como la tierra del sol naciente?", "respuesta": "japon"}
        ],
        "Deporte": [
            {"pregunta": "¿Qué deporte practica Michael Phelps?", "respuesta": "natacion"},
            {"pregunta": "¿Cuál es el grand slam que se juega sobre césped?", "respuesta": "wimbledon"},
            {"pregunta": "¿Cuántos jugadores componen un equipo de basket?", "respuesta": "cinco"},
            {"pregunta": "¿Cuál es el deporte que incluye el Tour de Francia?", "respuesta": "ciclismo"},
            {"pregunta": "¿En qué deporte se practica un Scrum?", "respuesta": "rugby"},
            {"pregunta": "¿A qué estás jugando si te acompaña un Caddie?", "respuesta": "golf"}
        ]
    }

    def menu_inicial():
        print("Bienvenido al ✨TRIVISTA✨")
        print("Instrucciones: ")
        print(" 1. Insertar la cantidad de jugadores ")
        print(" 2. Escoger una categoría y responder las preguntas correctamente para ganar.")
        print("3. Duelo de 2 jugadores, gana el mejor de 3 preguntas.")
        print("4. Duelo vs maquina: Compite contra el juego en una trivia a 5 preguntas.")

    def Participantes():
        cantidad_jugadores = int(input("¿Cuántos jugarán? (1 o 2): "))
        if cantidad_jugadores == 1 or cantidad_jugadores == 2:
            print(f"Cantidad de jugadores: {cantidad_jugadores}")
            return cantidad_jugadores
        else:
            print("Número no válido. Por favor, ingrese 1 o 2.")
            return Participantes()

    def Categorias():
        print("\nDisponibles:")
        print("Biología 🌱")
        print("Arte 🎬")
        print("Deporte 🏆")
        print("Geografía 🌎")

        categoria = input("Escoja una categoría: ").lower()
        if categoria == "biologia":
            return "Biología"
        elif categoria == "arte":
            return "Arte"
        elif categoria == "geografia":
            return "Geografía"
        elif categoria == "deporte":
            return "Deporte"
        else:
            print("Opción no válida. Intente nuevamente.")
            return Categorias()

    def iniciar_preguntas(categoria_elegida, cantidad_jugadores):
        preguntas = PreguntasTrivia[categoria_elegida]
        puntajes = [0] * cantidad_jugadores

        if cantidad_jugadores == 1:
            print("\n¡Juegas contra la máquina!")
            for pregunta in preguntas:
                respuesta_usuario = input(f"{pregunta['pregunta']} ")
                if respuesta_usuario.lower() == pregunta['respuesta']:
                    print("¡Correcto!")
                    puntajes[0] += 1
                else:
                    print(f"Incorrecto. La respuesta correcta es: {pregunta['respuesta']}")

            if puntajes[0] == len(preguntas):
                print("\n¡GANASTE!")
            else:
                print("\n¡PERDISTE!")

        elif cantidad_jugadores == 2:
            for i in range(cantidad_jugadores):
                print(f"\nTurno del Jugador {i + 1} en {categoria_elegida}")
                preguntas_jugador = preguntas[i * 3:(i + 1) * 3]
                for pregunta in preguntas_jugador:
                    respuesta_usuario = input(f"{pregunta['pregunta']} ")
                    if respuesta_usuario.lower() == pregunta['respuesta']:
                        print("¡Correcto!")
                        puntajes[i] += 1
                    else:
                        print(f"Incorrecto. La respuesta correcta es: {pregunta['respuesta']}")

            print("\nPuntaje final:")
            for i in range(cantidad_jugadores):
                print(f"Jugador {i + 1}: {puntajes[i]}")

            if puntajes[0] == puntajes[1]:
                print("\n¡EMPATE! Prueben otra categoría.")
                nueva_categoria = Categorias()
                iniciar_preguntas(nueva_categoria, cantidad_jugadores)
            else:
                max_puntaje = max(puntajes)
                ganador = puntajes.index(max_puntaje) + 1
                print(f"\nEl ganador es el Jugador {ganador} con {max_puntaje} puntos.")
    # Código principal
    while True:
        menu_inicial()
        cantidad_jugadores = Participantes()
        categoria = Categorias()
        iniciar_preguntas(categoria, cantidad_jugadores)
        
        opcion = input("\n¿Quieres volver al menú principal? (si/no): ").lower()
        if opcion == "no":
            print("Gracias por jugar. ¡Hasta pronto!")
            break
        elif opcion == "si":
            print("Regresando al Hub de Ingenio...")
        else:
            print("Opción inválida. Intente nuevamente.")

        

    def programa_2():
        print()
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
        2. Master
        3. juego de memoria
        4. Calculadora Multiusos.
        5. Salir.
        ''')
        try:
            opcion_principal = int(input("Seleccione una opción: "))
            
            if opcion_principal == 1:
                programa_1()
            elif opcion_principal == 2:
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
