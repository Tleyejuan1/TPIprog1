
# import pygame, sys, time, random, os

# pygame.init()
# # VARIABLE QUE CONTIENE EL TAMAÑO DE LA PANTALLA
# play_surface = pygame.display.set_mode((500, 500))
# # VARIABLE QUE CONTIENE LOS FPS
# #VARIABLE QUE CONTIENE EL TIPO DE LETRA
# fuente_letra = pygame.font.Font(None, 30)

# # Colores disponibles para la serpiente
# colores = {
#     1: (255, 0, 0),    # Rojo
#     2: (0, 255, 0),    # Verde
#     3: (0, 255, 255),  # Celeste
#     4: (0, 0, 255),    # Azul
#     5: (128, 0, 128)   # Violeta
# }

# def pedir_nombre_y_color():
#     #Pide al usuario el nombre y el color de la serpiente.
#     nombre = input("Ingresa el nombre de la serpiente: ")
#     print("Elige el color de la serpiente:")
#     print("1. Rojo")
#     print("2. Verde")
#     print("3. Celeste")
#     print("4. Azul")
#     print("5. Violeta")
    
#     # Ciclo para asegurar que el número del color esté en el rango correcto
#     color_opcion = None
#     while color_opcion not in colores:
#         try:
#             color_opcion = int(input("Ingresa el número del color elegido (1-5): "))
#             if color_opcion not in colores:
#                 print("Número ingresado incorrecto. Por favor elige un número entre 1 y 5.")
#         except ValueError:
#             print("Entrada inválida. Por favor ingresa un número.")
    
#     color = colores[color_opcion]
#     return nombre, color


# fps = pygame.time.Clock() #genera los pfs

# def comida(): #GENERA COMIDA DE FORMA RANDOM POR LA PANTALLA
#     random_pos = random.randint(0, 49) * 10
#     comida_pos = [random_pos, random_pos]
#     return comida_pos

# def guardar_puntuacion(nombre, puntaje):
#     """Guarda la puntuación en un archivo único con la puntuación máxima en la primera línea."""
#     max_puntuacion = obtener_maxima_puntuacion()
#     if puntaje > max_puntuacion:
#         max_puntuacion = puntaje
#     # Guardar la nueva puntuación máxima y todas las puntuaciones
#     with open("puntuaciones.txt", "w") as archivo:
#         archivo.write(f"Maxima puntuacion: {max_puntuacion}\n")
#         archivo.write(f"{nombre}: {puntaje}\n")
#         with open("puntuaciones.txt", "a") as archivo_2:
#             archivo_2.write(f"{nombre}: {puntaje}\n")
    
# def obtener_maxima_puntuacion():
#     """Obtiene la puntuación máxima de la primera línea del archivo."""
#     if not os.path.exists("puntuaciones.txt"):
#         return 0
#     with open("puntuaciones.txt", "r") as archivo:
#         primera_linea = archivo.readline().strip()
#         try:
#             max_puntuacion = int(primera_linea.split(": ")[1])
#         except (IndexError, ValueError):
#             max_puntuacion = 0
#     return max_puntuacion

# # CABEZA DE LA SERPIENTE
# def main():
#     nombre, color = pedir_nombre_y_color()
#     snake_cabeza = [100, 50] # PIXELES DE LA CABEZA DE LA SERPIENTE
#     snake_cuerpo = [[100, 50], [90, 50], [80, 50]] # PIXELES DE LA SERPIENTE EN EL CUERPO
#     sentido = "RIGHT" #MOVIMIENTO
#     run = True
#     comida_pos = comida()
#     puntaje = 0
#     max_puntuacion = obtener_maxima_puntuacion()
# #MOVIMIENTO DE LA SERPIENTE CUANDO SE TOCA DETERMINADA TECLA
#     while run:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 run = False
#             if event.type == pygame.KEYDOWN: # Variable que hace que la serpiente se mueva a la derecha cuando mueves el mouse
#                 if event.key == pygame.K_RIGHT:
#                     sentido = "RIGHT" 
#                 if event.key == pygame.K_LEFT:
#                     sentido = "LEFT" # Variable que hace que se mueva a la izquierda
#                 if event.key == pygame.K_UP:
#                     sentido = "UP"
#                 if event.key == pygame.K_DOWN:
#                     sentido = "DOWN"
        
#         # Movimiento de la serpiente
#         if sentido == "RIGHT":
#             snake_cabeza[0] += 10
#         if sentido == "LEFT":
#             snake_cabeza[0] -= 10
#         if sentido == "UP":
#             snake_cabeza[1] -= 10
#         if sentido == "DOWN":
#             snake_cabeza[1] += 10
        
#         # Actualizar el cuerpo de la serpiente
#         snake_cuerpo.insert(0, list(snake_cabeza))
        
#         if snake_cabeza == comida_pos: # HACE QUE CUANDO LA CABEZA DE LA SEPIENTE PASE POR UNA COMIDA SUME UN PUNTO
#             comida_pos = comida()
#             puntaje += 1
#             print(puntaje)
#         else:
#             snake_cuerpo.pop() # HACE QUE LA PARTE DE ATRAS DEL CUERPO DE LA SERPIENTE SE ELIMINE 
        
#         # Dibujar la pantalla y la serpiente
#         play_surface.fill((0, 0, 0)) # Hace la pantalla negra
#         for cabeza in snake_cuerpo:
#             pygame.draw.rect(play_surface, color, pygame.Rect(cabeza[0], cabeza[1], 10, 10)) # DIBUJA LA SERPIENTE EN EL COLOR ELEGIDO
            
#         texto = fuente_letra.render(f"Puntaje: {puntaje}", 0, (255, 0, 255)) #COLOR DE LA LETRA DEL PUNTAJE
#         play_surface.blit(texto, (380, 20)) #POSICIONA EL PUNTAJE ARRIBA A LA DERECHA
        
#         texto_max = fuente_letra.render(f"Max: {max_puntuacion}", 0, (255, 255, 0)) #COLOR DE LA LETRA DE LA PUNTUACION MAXIMA
#         play_surface.blit(texto_max, (10, 20)) #POSICIONA LA PUNTUACION MAXIMA ARRIBA A LA IZQUIERDA
        
#         texto_nombre = fuente_letra.render(f"Jugador: {nombre}", 0, (255, 255, 255)) #COLOR DE LA LETRA DEL NOMBRE
#         play_surface.blit(texto_nombre, (10, 50)) #POSICIONA EL NOMBRE DEL JUGADOR ARRIBA A LA IZQUIERDA
#         # VELOCIDAD DEL MOVIMIENTO DE LA SERPIENTE
#         if puntaje < 5: #CUANDO EL PUNTAJE SEA MENOR A 5 IRA A VELOCIDAD NORMAL
#             fps.tick(30)
#         if puntaje >= 10: # CUANDO EL PUNTAJE SEA MAYOR A 10 IRA MAS RAPIDO
#             fps.tick(50)
#         if puntaje >= 15:
#             fps.tick(70) # CUANDO EL PUNTAJE SEA 15 AUMENTA LA VELOCIDAD
        
#         if snake_cabeza[0] <= 0 or snake_cabeza[0] >= 500: #SI VAS A LA DERECHA DELTODO PERDES
#             run = False
#             print("PERDISTE")
#         if snake_cabeza[1] <= 0 or snake_cabeza[1] >= 500: #SI VAS A LA IZQUIERDA DELTODO PERDES
#             run= False
#             print("PERDISTE")
        
#         pygame.draw.rect(play_surface, (169, 6, 6), pygame.Rect(comida_pos[0], comida_pos[1], 9, 9)) #DIBUJA LA COMIDA EN ROJO
#         pygame.display.flip()
#         fps.tick(10)
    
#     guardar_puntuacion(nombre, puntaje)
#     pygame.quit()
#     sys.exit()

# main() 














# import pygame, sys, time, random, os

# pygame.init()
# # VARIABLE QUE CONTIENE EL TAMAÑO DE LA PANTALLA
# play_surface = pygame.display.set_mode((500, 500))
# # VARIABLE QUE CONTIENE LOS FPS
# #VARIABLE QUE CONTIENE EL TIPO DE LETRA
# fuente_letra = pygame.font.Font(None, 30)

# # Colores disponibles para la serpiente
# colores = {
#     1: (255, 0, 0),    # Rojo
#     2: (0, 255, 0),    # Verde
#     3: (0, 255, 255),  # Celeste
#     4: (0, 0, 255),    # Azul
#     5: (128, 0, 128)   # Violeta
# }

# def pedir_nombre_y_color():
#     #Pide al usuario el nombre y el color de la serpiente.
#     nombre = input("Ingresa el nombre de la serpiente: ")
#     print("Elige el color de la serpiente:")
#     print("1. Rojo")
#     print("2. Verde")
#     print("3. Celeste")
#     print("4. Azul")
#     print("5. Violeta")
    
#     # Ciclo para asegurar que el número del color esté en el rango correcto
#     color_opcion = None
#     while color_opcion not in colores:
#         try:
#             color_opcion = int(input("Ingresa el número del color elegido (1-5): "))
#             if color_opcion not in colores:
#                 print("Número ingresado incorrecto. Por favor elige un número entre 1 y 5.")
#         except ValueError:
#             print("Entrada inválida. Por favor ingresa un número.")
    
#     color = colores[color_opcion]
#     return nombre, color


# fps = pygame.time.Clock() #genera los pfs

# def comida(): #GENERA COMIDA DE FORMA RANDOM POR LA PANTALLA
#     random_pos = random.randint(0, 49) * 10
#     comida_pos = [random_pos, random_pos]
#     return comida_pos

# def guardar_puntuacion(nombre, puntaje):
#     """Guarda la puntuación en un archivo único con la puntuación máxima en la primera línea."""
#     max_puntuacion = obtener_maxima_puntuacion()
#     if puntaje > max_puntuacion:
#         max_puntuacion = puntaje
#     # Guardar la nueva puntuación máxima y todas las puntuaciones
#     with open("puntuaciones.txt", "w") as archivo:
#         archivo.write(f"Maxima puntuacion: {max_puntuacion}\n")
#         archivo.write(f"{nombre}: {puntaje}\n")
#         with open("puntuaciones.txt", "a") as archivo_2:
#             archivo_2.write(f"{nombre}: {puntaje}\n")
    
# def obtener_maxima_puntuacion():
#     """Obtiene la puntuación máxima de la primera línea del archivo."""
#     if not os.path.exists("puntuaciones.txt"):
#         return 0
#     with open("puntuaciones.txt", "r") as archivo:
#         primera_linea = archivo.readline().strip()
#         try:
#             max_puntuacion = int(primera_linea.split(": ")[1])
#         except (IndexError, ValueError):
#             max_puntuacion = 0
#     return max_puntuacion

# # CABEZA DE LA SERPIENTE
# def main():
#     nombre, color = pedir_nombre_y_color()
#     snake_cabeza = [100, 50] # PIXELES DE LA CABEZA DE LA SERPIENTE
#     snake_cuerpo = [[100, 50], [90, 50], [80, 50]] # PIXELES DE LA SERPIENTE EN EL CUERPO
#     sentido = "RIGHT" #MOVIMIENTO
#     run = True
#     comida_pos = comida()
#     puntaje = 0
#     max_puntuacion = obtener_maxima_puntuacion()
# #MOVIMIENTO DE LA SERPIENTE CUANDO SE TOCA DETERMINADA TECLA
#     while run:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 run = False
#             if event.type == pygame.KEYDOWN: # Variable que hace que la serpiente se mueva a la derecha cuando mueves el mouse
#                 if event.key == pygame.K_RIGHT:
#                     sentido = "RIGHT" 
#                 if event.key == pygame.K_LEFT:
#                     sentido = "LEFT" # Variable que hace que se mueva a la izquierda
#                 if event.key == pygame.K_UP:
#                     sentido = "UP"
#                 if event.key == pygame.K_DOWN:
#                     sentido = "DOWN"
        
#         # Movimiento de la serpiente
#         if sentido == "RIGHT":
#             snake_cabeza[0] += 10
#         if sentido == "LEFT":
#             snake_cabeza[0] -= 10
#         if sentido == "UP":
#             snake_cabeza[1] -= 10
#         if sentido == "DOWN":
#             snake_cabeza[1] += 10
        
#         # Actualizar el cuerpo de la serpiente
#         snake_cuerpo.insert(0, list(snake_cabeza))
        
#         if snake_cabeza == comida_pos: # HACE QUE CUANDO LA CABEZA DE LA SEPIENTE PASE POR UNA COMIDA SUME UN PUNTO
#             comida_pos = comida()
#             puntaje += 1
#             print(puntaje)
#         else:
#             snake_cuerpo.pop() # HACE QUE LA PARTE DE ATRAS DEL CUERPO DE LA SERPIENTE SE ELIMINE 
        
#         # Dibujar la pantalla y la serpiente
#         play_surface.fill((0, 0, 0)) # Hace la pantalla negra
#         for cabeza in snake_cuerpo:
#             pygame.draw.rect(play_surface, color, pygame.Rect(cabeza[0], cabeza[1], 10, 10)) # DIBUJA LA SERPIENTE EN EL COLOR ELEGIDO
            
#         texto = fuente_letra.render(f"Puntaje: {puntaje}", 0, (255, 0, 255)) #COLOR DE LA LETRA DEL PUNTAJE
#         play_surface.blit(texto, (380, 20)) #POSICIONA EL PUNTAJE ARRIBA A LA DERECHA
        
#         texto_max = fuente_letra.render(f"Max: {max_puntuacion}", 0, (255, 255, 0)) #COLOR DE LA LETRA DE LA PUNTUACION MAXIMA
#         play_surface.blit(texto_max, (10, 20)) #POSICIONA LA PUNTUACION MAXIMA ARRIBA A LA IZQUIERDA
        
#         texto_nombre = fuente_letra.render(f"Jugador: {nombre}", 0, (255, 255, 255)) #COLOR DE LA LETRA DEL NOMBRE
#         play_surface.blit(texto_nombre, (10, 50)) #POSICIONA EL NOMBRE DEL JUGADOR ARRIBA A LA IZQUIERDA
#         # VELOCIDAD DEL MOVIMIENTO DE LA SERPIENTE
#         if puntaje < 5: #CUANDO EL PUNTAJE SEA MENOR A 5 IRA A VELOCIDAD NORMAL
#             fps.tick(30)
#         if puntaje >= 10: # CUANDO EL PUNTAJE SEA MAYOR A 10 IRA MAS RAPIDO
#             fps.tick(50)
#         if puntaje >= 15:
#             fps.tick(70) # CUANDO EL PUNTAJE SEA 15 AUMENTA LA VELOCIDAD
        
#         if snake_cabeza[0] <= 0 or snake_cabeza[0] >= 500: #SI VAS A LA DERECHA DELTODO PERDES
#             run = False
#             print("PERDISTE")
#         if snake_cabeza[1] <= 0 or snake_cabeza[1] >= 500: #SI VAS A LA IZQUIERDA DELTODO PERDES
#             run= False
#             print("PERDISTE")
        
#         pygame.draw.rect(play_surface, (169, 6, 6), pygame.Rect(comida_pos[0], comida_pos[1], 9, 9)) #DIBUJA LA COMIDA EN ROJO
#         pygame.display.flip()
#         fps.tick(10)
    
#     guardar_puntuacion(nombre, puntaje)
#     pygame.quit()
#     sys.exit()

# main()



import pygame
import sys
import random

pygame.init()

# VARIABLES GLOBALES
play_surface = pygame.display.set_mode((500, 500))
fuente_letra = pygame.font.Font(None, 30)
fps = pygame.time.Clock()

# COLORES
colores = {
    1: (255, 0, 0),
    2: (0, 255, 0),
    3: (0, 255, 255),
    4: (0, 0, 255),
    5: (128, 0, 128)
}


def pedir_nombre_y_color(jugador_num):
    print(f"\nJugador {jugador_num}:")
    nombre = input("Ingresa el nombre de la serpiente: ")
    print("Elige el color de la serpiente:")
    for k, v in colores.items():
        print(f"{k}. {['Rojo', 'Verde', 'Celeste', 'Azul', 'Violeta'][k - 1]}")
    color_opcion = None
    while color_opcion not in colores:
        try:
            color_opcion = int(input("Ingresa el número del color elegido (1-5): "))
            if color_opcion not in colores:
                print("Número incorrecto. Elige entre 1 y 5.")
        except ValueError:
            print("Entrada inválida. Ingresa un número.")
    return f"Jugador {jugador_num} - {nombre}", colores[color_opcion]


def comida():
    random_pos = random.randint(0, 49) * 10
    return [random_pos, random_pos]


def guardar_puntuaciones(jugadores):
    mayor_puntaje = max(jugadores, key=lambda x: x[1])
    with open("puntuaciones.txt", "w") as archivo:
        archivo.write(f"¡¡GANADOR CON MÁXIMA PUNTUACIÓN:!! {mayor_puntaje[0]} - {mayor_puntaje[1]}\n")
        for jugador, puntaje in jugadores:
            archivo.write(f"{jugador}: {puntaje}\n")


def jugar_partida(nombre, color):
    snake_cabeza = [100, 50]
    snake_cuerpo = [[100, 50], [90, 50], [80, 50]]
    sentido = "RIGHT"
    comida_pos = comida()
    puntaje = 0
    max_puntuacion = 0
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and sentido != "LEFT":
                    sentido = "RIGHT"
                elif event.key == pygame.K_LEFT and sentido != "RIGHT":
                    sentido = "LEFT"
                elif event.key == pygame.K_UP and sentido != "DOWN":
                    sentido = "UP"
                elif event.key == pygame.K_DOWN and sentido != "UP":
                    sentido = "DOWN"

        # Movimiento de la serpiente
        if sentido == "RIGHT":
            snake_cabeza[0] += 10
        elif sentido == "LEFT":
            snake_cabeza[0] -= 10
        elif sentido == "UP":
            snake_cabeza[1] -= 10
        elif sentido == "DOWN":
            snake_cabeza[1] += 10

        snake_cuerpo.insert(0, list(snake_cabeza))
        if snake_cabeza == comida_pos:
            comida_pos = comida()
            puntaje += 1
            max_puntuacion = max(max_puntuacion, puntaje)
        else:
            snake_cuerpo.pop()

        # Dibujar elementos
        play_surface.fill((0, 0, 0))
        for bloque in snake_cuerpo:
            pygame.draw.rect(play_surface, color, pygame.Rect(bloque[0], bloque[1], 10, 10))
        pygame.draw.rect(play_surface, (169, 6, 6), pygame.Rect(comida_pos[0], comida_pos[1], 9, 9))

        texto_puntaje = fuente_letra.render(f"Puntaje: {puntaje}", 0, (255, 0, 255))
        texto_max = fuente_letra.render(f"Max: {max_puntuacion}", 0, (255, 255, 0))
        texto_nombre = fuente_letra.render(f"Jugador: {nombre}", 0, (255, 255, 255))
        play_surface.blit(texto_puntaje, (380, 20))
        play_surface.blit(texto_max, (10, 20))
        play_surface.blit(texto_nombre, (10, 50))

        # Actualizar pantalla
        pygame.display.flip()
        if puntaje < 5:
            fps.tick(10)
        elif puntaje < 10:
            fps.tick(15)
        else:
            fps.tick(20)

        # Verificar colisiones
        if snake_cabeza[0] < 0 or snake_cabeza[0] >= 500 or snake_cabeza[1] < 0 or snake_cabeza[1] >= 500:
            run = False
            print("PERDISTE")

    return puntaje


def main():
    jugadores = []
    for i in range(1, 4):
        nombre, color = pedir_nombre_y_color(i)
        jugadores.append((nombre, color))

    resultados = []
    for nombre, color in jugadores:
        puntaje = jugar_partida(nombre, color)
        resultados.append((nombre, puntaje))

    guardar_puntuaciones(resultados)


if __name__ == "__main__":
    main()
