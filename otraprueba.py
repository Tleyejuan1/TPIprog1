import pygame, sys, time, random, os

pygame.init()
play_surface = pygame.display.set_mode((500, 500))
fuente_letra = pygame.font.Font(None, 30)

colores = {
    1: (255, 0, 0),
    2: (0, 255, 0),
    3: (0, 255, 255),
    4: (0, 0, 255),
    5: (128, 0, 128)
}

def pedir_nombre_y_color():
    nombre = input("Ingresa el nombre de la serpiente: ")
    print("Elige el color de la serpiente:")
    print("1. Rojo\n2. Verde\n3. Celeste\n4. Azul\n5. Violeta")

    color_opcion = None
    while color_opcion not in colores:
        try:
            color_opcion = int(input("Ingresa el número del color elegido (1-5): "))
            if color_opcion not in colores:
                print("Número ingresado incorrecto. Por favor elige un número entre 1 y 5.")
        except ValueError:
            print("Entrada inválida. Por favor ingresa un número.")
    
    color = colores[color_opcion]
    return nombre, color

fps = pygame.time.Clock()

def comida():
    random_pos = random.randint(0, 49) * 10
    return [random_pos, random_pos]

def guardar_puntuacion(nombre, puntaje):
    max_puntuacion = obtener_maxima_puntuacion()
    
    with open("puntuaciones.txt", "a") as archivo:
        archivo.write(f"{nombre}: {puntaje}\n")
    
    if puntaje > max_puntuacion:
        with open("puntuaciones.txt", "r") as archivo:
            lineas = archivo.readlines()
        
        with open("puntuaciones.txt", "w") as archivo:
            archivo.write(f"Maxima puntuacion: {nombre} - {puntaje}\n")
            archivo.writelines(lineas[1:])  # Mantener todas las puntuaciones anteriores

def obtener_maxima_puntuacion():
    if not os.path.exists("puntuaciones.txt"):
        return 0
    with open("puntuaciones.txt", "r") as archivo:
        primera_linea = archivo.readline().strip()
        try:
            max_jugador, max_puntuacion = primera_linea.split(": ")[1].split(" - ")
            return int(max_puntuacion)
        except (IndexError, ValueError):
            return 0

def main():
    nombre, color = pedir_nombre_y_color()
    snake_cabeza = [100, 50]
    snake_cuerpo = [[100, 50], [90, 50], [80, 50]]
    sentido = "RIGHT"
    run = True
    comida_pos = comida()
    puntaje = 0
    max_puntuacion = obtener_maxima_puntuacion()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT: sentido = "RIGHT" 
                if event.key == pygame.K_LEFT: sentido = "LEFT"
                if event.key == pygame.K_UP: sentido = "UP"
                if event.key == pygame.K_DOWN: sentido = "DOWN"
        
        if sentido == "RIGHT": snake_cabeza[0] += 10
        if sentido == "LEFT": snake_cabeza[0] -= 10
        if sentido == "UP": snake_cabeza[1] -= 10
        if sentido == "DOWN": snake_cabeza[1] += 10
        
        snake_cuerpo.insert(0, list(snake_cabeza))
        
        if snake_cabeza == comida_pos:
            comida_pos = comida()
            puntaje += 1
            print(puntaje)
        else:
            snake_cuerpo.pop()
        
        play_surface.fill((0, 0, 0))
        for cabeza in snake_cuerpo:
            pygame.draw.rect(play_surface, color, pygame.Rect(cabeza[0], cabeza[1], 10, 10))
            
        texto = fuente_letra.render(f"Puntaje: {puntaje}", 0, (255, 0, 255))
        play_surface.blit(texto, (380, 20))
        
        texto_max = fuente_letra.render(f"Max: {max_puntuacion}", 0, (255, 255, 0))
        play_surface.blit(texto_max, (10, 20))
        
        texto_nombre = fuente_letra.render(f"Jugador: {nombre}", 0, (255, 255, 255))
        play_surface.blit(texto_nombre, (10, 50))
        
        if puntaje < 5:
            fps.tick(30)
        if puntaje >= 10:
            fps.tick(50)
        if puntaje >= 15:
            fps.tick(70)
        
        if snake_cabeza[0] <= 0 or snake_cabeza[0] >= 500 or snake_cabeza[1] <= 0 or snake_cabeza[1] >= 500:
            run = False
            print("PERDISTE")
        
        pygame.draw.rect(play_surface, (169, 6, 6), pygame.Rect(comida_pos[0], comida_pos[1], 9, 9))
        pygame.display.flip()
        fps.tick(10)
    
    guardar_puntuacion(nombre, puntaje)
    pygame.quit()
    sys.exit()

main()
