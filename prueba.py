def programa_principal():
    while True:
        print('''
        Menú Principal:
        1. Juego de Trivia.
        2. Snake game.
        3. Juego de Memoria.
        4. Calculadora Multiusos.
        5. Salir.
        ''')
        try:
            opcion_principal = int(input("Seleccione una opción: "))
            if opcion_principal == 1:
                programa_1()  # Llamada a programa_1
            # elif opcion_principal == 2:
            #     programa_2()  # Llamada al Snake Game (descomentar cuando exista)
            # elif opcion_principal == 3:
            #     juego_memoria()  # Llamada al Juego de Memoria
            # elif opcion_principal == 4:
            #     calculadora()  # Llamada a Calculadora
            elif opcion_principal == 5:
                print("Saliendo del programa...")
                break  # Finaliza el bucle del programa principal
            else:
                print("Opción inválida. Intente de nuevo.")
        except ValueError:
            print("Error: Por favor ingrese un número válido.")


def programa_1():
    preguntas_trivia = {
        "Biología": [
            {"pregunta": "¿Cuál es el tipo de célula que NO tiene núcleo?", "respuesta": "procariota"},
            {"pregunta": "¿Cuál es la molécula que almacena la información genética?", "respuesta": "adn"},
            {"pregunta": "¿Cómo se llama el proceso por el cual las plantas producen su alimento?", "respuesta": "fotosintesis"},
            {"pregunta": "¿Cuál es el hueso más largo del cuerpo humano?", "respuesta": "femur"},
            {"pregunta": "¿Cuál es el mamífero que puede volar?", "respuesta": "murcielago"},
            {"pregunta": "¿Cuál es el depredador más grande de la tierra?", "respuesta": "orca"}
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

    def menu_principal():
        print("\n✨ ¡Bienvenido al TRIVISTA! ✨")
        print("Instrucciones:")
        print("1. Insertar cantidad de jugadores.")
        print("2. Escoger una categoría y responder las preguntas correctamente para ganar.")
        print("3. Duelo de 2 jugadores: gana el mejor de 3 preguntas.")
        print("4. Duelo contra la máquina: trivia de 5 preguntas.")

    def participantes():
        while True:
            try:
                cantidad = int(input("¿Cuántos jugarán? (1 o 2): "))
                if cantidad in [1, 2]:
                    return cantidad
                else:
                    print("Por favor, elija 1 o 2 jugadores.")
            except ValueError:
                print("Entrada inválida. Por favor ingrese un número.")

    def categorias():
        print("\nCategorías disponibles:")
        print("1. Biología 🌱")
        print("2. Arte 🎬")
        print("3. Deporte 🏆")
        print("4. Geografía 🌎")
        opciones = {"1": "Biología", "2": "Arte", "3": "Deporte", "4": "Geografía"}
        while True:
            opcion = input("Elija una categoría (1-4): ")
            if opcion in opciones:
                return opciones[opcion]
            else:
                print("Opción no válida. Intente nuevamente.")

    def iniciar_preguntas(categoria, jugadores):
        preguntas = preguntas_trivia[categoria]
        puntajes = [0] * jugadores
        preguntas_a_jugar = preguntas[:5] if jugadores == 1 else preguntas[:6]

        print("\n¡Iniciando el juego!")
        for i, pregunta in enumerate(preguntas_a_jugar):
            respuesta = input(f"{i + 1}. {pregunta['pregunta']}: ").lower()
            if respuesta == pregunta['respuesta']:
                print("¡Correcto!")
                puntajes[i % jugadores] += 1
            else:
                print(f"Incorrecto. La respuesta era: {pregunta['respuesta']}.")

        print("\nResultados:")
        for i, puntos in enumerate(puntajes):
            print(f"Jugador {i + 1}: {puntos} puntos.")

    menu_principal()
    cantidad_jugadores = participantes()
    categoria = categorias()
    iniciar_preguntas(categoria, cantidad_jugadores)


# Llamar al programa principal
programa_principal()
