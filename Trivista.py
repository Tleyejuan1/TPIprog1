PreguntasTrivia= {
    "Biologia": [
        {"pregunta": "¿Cual es el tipo de celula que no tiene nucleo?", "respuesta": "procariota"},
        {"pregunta": "¿Cual es la molecula que almacena la informacion genetica?", "respuesta": "ADN"},
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

menu_inicial()
cantidad_jugadores = Participantes()
categoria = Categorias()
iniciar_preguntas(categoria, cantidad_jugadores)
