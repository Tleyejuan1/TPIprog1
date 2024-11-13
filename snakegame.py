
import pygame, sys, random

# INICIALIZA PYGAME
pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500 #TAMAÑO DE LA PANTALLA
play_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
fps = pygame.time.Clock()

# COLORES QUE EL USUARIO PUEDE ELIGIR PARA LA SERPIENTE
colores = {
    1: (255, 0, 0),    # Rojo
    2: (0, 255, 0),    # Verde
    3: (0, 255, 255),  # Celeste
    4: (0, 0, 255),    # Azul
    5: (128, 0, 128)   # Violeta
}

# FUENTE DE LETRA PARA EL PUNTAJE
fuente_letra = pygame.font.Font(None, 30)

# ARCHIVO DONDE SE GUARDA EL PUNTAJE MAXIMO
archivo_puntaje = "puntaje_maximo.txt"

def main():
    nombre = input("Ingresa el nombre de la serpiente: ") #NOMBRE DE LA SERPIENTE
    print("Elige el color de la serpiente: 1-Rojo, 2-Verde, 3-Celeste, 4-Azul, 5-Violeta")
    color_opcion = int(input("Elige un número (1-5): "))
    color = colores.get(color_opcion, (0, 255, 0))  # Verde por defecto

    # Inicialización de la serpiente y el puntaje
    snake_cabeza = [100, 50]
    snake_cuerpo = [[100, 50], [90, 50], [80, 50]]
    change = "RIGHT"
    comida_pos = [random.randint(0, 49) * 10, random.randint(0, 49) * 10]
    puntaje = 0

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and change != "LEFT":
                    change = "RIGHT"
                if event.key == pygame.K_LEFT and change != "RIGHT":
                    change = "LEFT"
                if event.key == pygame.K_UP and change != "DOWN":
                    change = "UP"
                if event.key == pygame.K_DOWN and change != "UP":
                    change = "DOWN"

        # MOVIMIENTO DE LA SERPIENTE
        if change == "RIGHT": #DERECHA
            snake_cabeza[0] += 10
        if change == "LEFT": #IZQUIERDA
            snake_cabeza[0] -= 10
        if change == "UP": #SUBE
            snake_cabeza[1] -= 10
        if change == "DOWN": #BAJ
            snake_cabeza[1] += 10
        snake_cuerpo.insert(0, list(snake_cabeza))

        # CUANDO "COME" LA COMIDA CRECE
        if snake_cabeza == comida_pos:
            comida_pos = [random.randint(0, 49) * 10, random.randint(0, 49) * 10]
            puntaje += 1
        else:
            snake_cuerpo.pop()

        # LIMITES DE LA PANTALLA
        if snake_cabeza[0] <= 0 or snake_cabeza[0] >= SCREEN_WIDTH or snake_cabeza[1] <= 0 or snake_cabeza[1] >= SCREEN_HEIGHT:
            print(f"{nombre} PERDISTE")
            run = False

        # CHEQUEAR SI SE COMIO A SI MISMA
        play_surface.fill((0, 0, 0))  # PANTALLA NEGRA
        for parte in snake_cuerpo:
            pygame.draw.rect(play_surface, color, pygame.Rect(parte[0], parte[1], 10, 10))
        pygame.draw.rect(play_surface, (169, 6, 6), pygame.Rect(comida_pos[0], comida_pos[1], 9, 9))

        texto = fuente_letra.render(f"{nombre}: {puntaje}", 0, (255, 0, 255))
        play_surface.blit(texto, (320, 20))
        pygame.display.flip()

        # VELOCIDAD DEL JUEGO SEGUN EL PUNTAJE
        if puntaje < 5:
            fps.tick(10)
        if puntaje < 10:
            fps.tick(15)
        if puntaje > 15:
            fps.tick(20)
            
    # SE GUARDA EL PUNTAJE CUANDO PIERDE
    try:
        with open(archivo_puntaje, "r") as file:
            puntaje_maximo = int(file.read())
    except FileNotFoundError:
        puntaje_maximo = 0

    if puntaje > puntaje_maximo:
        print(f"¡Nuevo puntaje más alto: {puntaje}!")
        with open(archivo_puntaje, "w") as file:
            file.write(str("¡¡NUEVO RECORD!!"(puntaje)))
    else:
        print(f"El puntaje más alto actual es: {puntaje_maximo}")

    pygame.quit()
    sys.exit()

main()
