# import pygame, sys, random #INSTALA DRIVERS Q HACEN POSIBLE EL JUEGO

# pygame.init()
# # VARIABLE QUE CONTIENE EL TAMAÑO DE LA PANTALLA
# play_surface = pygame.display.set_mode((500, 500))
# # VARIABLE QUE CONTIENE LOS FPS
# # VARIABLE QUE CONTIENE EL TIPO DE LETRA
# fuente_letra = pygame.font.Font(None, 30)

# #COLORES DE LA SERPIENTE
# colores = {
#     1: (255, 0, 0),    # ROJO
#     2: (0, 255, 0),    # VERDE
#     3: (0, 255, 255),  # CELESTE
#     4: (0, 0, 255),    # AZUL
#     5: (128, 0, 128)   # VIOLETA
# }

# def pedir_nombre_y_color(jugador_num): #PEDIR NOMBRE DE USUARIO Y COLOR
#     print(f"\nJugador {jugador_num}:")
#     nombre = input("Ingresa el nombre de la serpiente: ")
#     print("Elige el color de la serpiente:")
#     print("1. Rojo")
#     print("2. Verde")
#     print("3. Celeste")
#     print("4. Azul")
#     print("5. Violeta")
    
#     #CICLO DE NUMERO CORRECTO
#     color_opcion = None
#     while color_opcion not in colores:
#         try:
#             color_opcion = int(input("Ingresa el número del color elegido (1-5): "))
#             if color_opcion not in colores:
#                 print("Número ingresado incorrecto. Por favor elige un número entre 1 y 5.")
#         except ValueError:
#             print("Entrada inválida. Por favor ingresa un número.")
    
#     color = colores[color_opcion]
#     return f"Jugador {jugador_num} - {nombre}", color


# fps = pygame.time.Clock()  #PONE LOS FPS DEL PROFRAMA

# def comida():  #GENERA COMIDA DE FORMA RANDOM POR LA PANTALLA
#     random_pos = random.randint(0, 49) * 10
#     comida_pos = [random_pos, random_pos]
#     return comida_pos

# def guardar_puntuaciones(jugadores): #GUARDA LAS PUNTUACIONES DE LOS JUGADORES
#     mayor_puntaje = max(jugadores, key=lambda x: x[1])  #JUGADOR CON MAYOR PUNTAJE
#     with open("puntuaciones.txt", "w") as archivo:
#         archivo.write(f"¡¡GANADOR CON MAXIMA PUNTUACION:!! {mayor_puntaje[0]} - {mayor_puntaje[1]}\n")
#         for jugador, puntaje in jugadores:
#             archivo.write(f"{jugador}: {puntaje}\n")

# def main(): #FOR DE LOS 3 JUGADORES Q PARTICPAN
#     jugadores = []
#     for i in range(1, 4):  # ITERA LOS JUGADORES 1, 2 y 3
#         nombre, color = pedir_nombre_y_color(i)
#         jugadores.append((nombre, color))

#     resultados = []  #GUARDA EL PUNTAJE DE CADA JUGADOR

#     #CUCLE DE JUEGO C/U
#     for nombre, color in jugadores:
#         snake_cabeza = [100, 50]
#         snake_cuerpo = [[100, 50], [90, 50], [80, 50]]
#         sentido = "RIGHT"
#         run = True
#         comida_pos = comida()
#         puntaje = 0
#         max_puntuacion = 0  #PUNTUACION MAXIMA

#         # MOVIMIENTO DE LA SERPIENTE CUANDO SE TOCA DETERMINADA TECLA
#         while run:
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     pygame.quit()
#                     sys.exit()
#                 if event.type == pygame.KEYDOWN:  #VARIABLE QUE HACE Q LA SERPIENTE PUEDA MOVERSE CON LAS TECLAS
#                     if event.key == pygame.K_RIGHT:
#                         sentido = "RIGHT" #SE MUEVE A LA DERECHA
#                     if event.key == pygame.K_LEFT:
#                         sentido = "LEFT"  #SE MUEVE IZQUIERDA
#                     if event.key == pygame.K_UP:
#                         sentido = "UP" #SE MUEVE ARRIBA
#                     if event.key == pygame.K_DOWN:
#                         sentido = "DOWN" # SE MUEVE ABAJO

#             #MOVIMIENO DE LA SERPIENTE
#             if sentido == "RIGHT":
#                 snake_cabeza[0] += 10
#             if sentido == "LEFT":
#                 snake_cabeza[0] -= 10
#             if sentido == "UP":
#                 snake_cabeza[1] -= 10
#             if sentido == "DOWN":
#                 snake_cabeza[1] += 10

#             # Actualizar el cuerpo de la serpiente
#             snake_cuerpo.insert(0, list(snake_cabeza))
            
#             if snake_cabeza == comida_pos:  # HACE QUE CUANDO LA CABEZA DE LA SERPIENTE PASE POR UNA COMIDA SUME UN PUNTO
#                 comida_pos = comida()
#                 puntaje += 1
#                 max_puntuacion = max(max_puntuacion, puntaje)
#                 print(puntaje)
#             else:
#                 snake_cuerpo.pop()  # HACE QUE LA PARTE DE ATRÁS DEL CUERPO DE LA SERPIENTE SE ELIMINE

#             #DIBUJOS DE PANTALLA Y SERPIENTE
#             play_surface.fill((0, 0, 0))  #HACE LA PANTALLA NEGRA
#             for cabeza in snake_cuerpo:
#                 pygame.draw.rect(play_surface, color, pygame.Rect(cabeza[0], cabeza[1], 10, 10))  #DIBUJA LA SERPIENTE EN EL COLOR ELEGIDO

#             texto = fuente_letra.render(f"Puntaje: {puntaje}", 0, (255, 0, 255))  #COLOR DE LA LETRA DEL PUNTAJE
#             play_surface.blit(texto, (380, 20))  #POSICIONA EL PUNTAJE ARRIBA A LA DERECHA
            
#             texto_max = fuente_letra.render(f"Max: {max_puntuacion}", 0, (255, 255, 0))  #COLOR DE LA LETRA DE LA PUNTUACIÓN MÁXIMA
#             play_surface.blit(texto_max, (10, 20))  #POSICIONA LA PUNTUACIÓN MÁXIMA ARRIBA A LA IZQUIERDA
            
#             texto_nombre = fuente_letra.render(f"Jugador: {nombre}", 0, (255, 255, 255))  #COLOR DE LA LETRA DEL NOMBRE
#             play_surface.blit(texto_nombre, (10, 50))  #POSICIONA EL NOMBRE DEL JUGADOR ARRIBA A LA IZQUIERDA
#             #VELOCIDAD DEL MOVIMIENTO DE LA SERPIENTE
#             if puntaje < 5:  #CUANDO EL PUNTAJE SEA MENOR A 5 IRA A VELOCIDAD NORMAL
#                 fps.tick(10)
#             elif puntaje < 10:  #CUANDO EL PUNTAJE SEA MAYOR A 5 PERO MENOR A 10
#                 fps.tick(15)
#             else:  #CUANDO EL PUNTAJE SEA 10 O MÁS
#                 fps.tick(20)

#             if snake_cabeza[0] < 0 or snake_cabeza[0] >= 500 or snake_cabeza[1] < 0 or snake_cabeza[1] >= 500: #PARAMETROS DE LA PANTALLA SI SE SALE PIERDE
#                 run = False
#                 print("PERDISTE")

#             pygame.draw.rect(play_surface, (169, 6, 6), pygame.Rect(comida_pos[0], comida_pos[1], 9, 9))  #DIBUJA LA COMIDA EN ROJO
#             pygame.display.flip()
        
#         resultados.append((nombre, puntaje))

#     guardar_puntuaciones(resultados)

# main()





import pygame, sys, random #INSTALA DRIVERS Q HACEN POSIBLE EL JUEGO

def jugar_snake():
    pygame.init()
    # VARIABLE QUE CONTIENE EL TAMAÑO DE LA PANTALLA
    play_surface = pygame.display.set_mode((500, 500))
    # VARIABLE QUE CONTIENE LOS FPS
    # VARIABLE QUE CONTIENE EL TIPO DE LETRA
    fuente_letra = pygame.font.Font(None, 30)

    #COLORES DE LA SERPIENTE
    colores = {
        1: (255, 0, 0),    # ROJO
        2: (0, 255, 0),    # VERDE
        3: (0, 255, 255),  # CELESTE
        4: (0, 0, 255),    # AZUL
        5: (128, 0, 128)   # VIOLETA
    }

    def pedir_nombre_y_color(jugador_num): #PEDIR NOMBRE DE USUARIO Y COLOR
        print(f"\nJugador {jugador_num}:")
        nombre = input("Ingresa el nombre de la serpiente: ")
        print("Elige el color de la serpiente:")
        print("1. Rojo")
        print("2. Verde")
        print("3. Celeste")
        print("4. Azul")
        print("5. Violeta")
        
        #CICLO DE NUMERO CORRECTO
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


    fps = pygame.time.Clock()  #PONE LOS FPS DEL PROFRAMA

    def comida():  #GENERA COMIDA DE FORMA RANDOM POR LA PANTALLA
        random_pos = random.randint(0, 49) * 10
        comida_pos = [random_pos, random_pos]
        return comida_pos

    def guardar_puntuaciones(jugadores): #GUARDA LAS PUNTUACIONES DE LOS JUGADORES
        mayor_puntaje = max(jugadores, key=lambda x: x[1])  #JUGADOR CON MAYOR PUNTAJE
        with open("puntuaciones.txt", "w") as archivo:
            archivo.write(f"¡¡GANADOR CON MAXIMA PUNTUACION:!! {mayor_puntaje[0]} - {mayor_puntaje[1]}\n")
            for jugador, puntaje in jugadores:
                archivo.write(f"{jugador}: {puntaje}\n")

    def main(): #FOR DE LOS 3 JUGADORES Q PARTICPAN
        jugadores = []
        for i in range(1, 4):  # ITERA LOS JUGADORES 1, 2 y 3
            nombre, color = pedir_nombre_y_color(i)
            jugadores.append((nombre, color))

        resultados = []  #GUARDA EL PUNTAJE DE CADA JUGADOR

        #CUCLE DE JUEGO C/U
        for nombre, color in jugadores:
            snake_cabeza = [100, 50]
            snake_cuerpo = [[100, 50], [90, 50], [80, 50]]
            sentido = "RIGHT"
            run = True
            comida_pos = comida()
            puntaje = 0
            max_puntuacion = 0  #PUNTUACION MAXIMA

            # MOVIMIENTO DE LA SERPIENTE CUANDO SE TOCA DETERMINADA TECLA
            while run:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:  #VARIABLE QUE HACE Q LA SERPIENTE PUEDA MOVERSE CON LAS TECLAS
                        if event.key == pygame.K_RIGHT:
                            sentido = "RIGHT" #SE MUEVE A LA DERECHA
                        if event.key == pygame.K_LEFT:
                            sentido = "LEFT"  #SE MUEVE IZQUIERDA
                        if event.key == pygame.K_UP:
                            sentido = "UP" #SE MUEVE ARRIBA
                        if event.key == pygame.K_DOWN:
                            sentido = "DOWN" # SE MUEVE ABAJO

                #MOVIMIENO DE LA SERPIENTE
                if sentido == "RIGHT":
                    snake_cabeza[0] += 10
                if sentido == "LEFT":
                    snake_cabeza[0] -= 10
                if sentido == "UP":
                    snake_cabeza[1] -= 10
                if sentido == "DOWN":
                    snake_cabeza[1] += 10

                # Actualizar el cuerpo de la serpiente
                snake_cuerpo.insert(0, list(snake_cabeza))
                
                if snake_cabeza == comida_pos:  # HACE QUE CUANDO LA CABEZA DE LA SERPIENTE PASE POR UNA COMIDA SUME UN PUNTO
                    comida_pos = comida()
                    puntaje += 1
                    max_puntuacion = max(max_puntuacion, puntaje)
                    print(puntaje)
                else:
                    snake_cuerpo.pop()  # HACE QUE LA PARTE DE ATRÁS DEL CUERPO DE LA SERPIENTE SE ELIMINE

                #DIBUJOS DE PANTALLA Y SERPIENTE
                play_surface.fill((0, 0, 0))  #HACE LA PANTALLA NEGRA
                for cabeza in snake_cuerpo:
                    pygame.draw.rect(play_surface, color, pygame.Rect(cabeza[0], cabeza[1], 10, 10))  #DIBUJA LA SERPIENTE EN EL COLOR ELEGIDO

                texto = fuente_letra.render(f"Puntaje: {puntaje}", 0, (255, 0, 255))  #COLOR DE LA LETRA DEL PUNTAJE
                play_surface.blit(texto, (380, 20))  #POSICIONA EL PUNTAJE ARRIBA A LA DERECHA
                
                texto_max = fuente_letra.render(f"Max: {max_puntuacion}", 0, (255, 255, 0))  #COLOR DE LA LETRA DE LA PUNTUACIÓN MÁXIMA
                play_surface.blit(texto_max, (10, 20))  #POSICIONA LA PUNTUACIÓN MÁXIMA ARRIBA A LA IZQUIERDA
                
                texto_nombre = fuente_letra.render(f"Jugador: {nombre}", 0, (255, 255, 255))  #COLOR DE LA LETRA DEL NOMBRE
                play_surface.blit(texto_nombre, (10, 50))  #POSICIONA EL NOMBRE DEL JUGADOR ARRIBA A LA IZQUIERDA
                #VELOCIDAD DEL MOVIMIENTO DE LA SERPIENTE
                if puntaje < 5:  #CUANDO EL PUNTAJE SEA MENOR A 5 IRA A VELOCIDAD NORMAL
                    fps.tick(10)
                elif puntaje < 10:  #CUANDO EL PUNTAJE SEA MAYOR A 5 PERO MENOR A 10
                    fps.tick(15)
                else:  #CUANDO EL PUNTAJE SEA 10 O MÁS
                    fps.tick(20)

                if snake_cabeza[0] < 0 or snake_cabeza[0] >= 500 or snake_cabeza[1] < 0 or snake_cabeza[1] >= 500: #PARAMETROS DE LA PANTALLA SI SE SALE PIERDE
                    run = False
                    print("PERDISTE")

                pygame.draw.rect(play_surface, (169, 6, 6), pygame.Rect(comida_pos[0], comida_pos[1], 9, 9))  #DIBUJA LA COMIDA EN ROJO
                pygame.display.flip()
            
            resultados.append((nombre, puntaje))

        guardar_puntuaciones(resultados)

# Puedes llamar a esta función para ejecutar el juego
# jugar_snake()
