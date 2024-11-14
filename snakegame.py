
import pygame, sys, time, random, os

pygame.init()
# VARIABLE QUE CONTIENE EL TAMAÑO DE LA PANTALLA
play_surface = pygame.display.set_mode((500, 500))
# VARIABLE QUE CONTIENE LOS FPS

fuente_letra = pygame.font.Font(None, 30)

# Colores disponibles para la serpiente
colores = {
    1: (255, 0, 0),    # Rojo
    2: (0, 255, 0),    # Verde
    3: (0, 255, 255),  # Celeste
    4: (0, 0, 255),    # Azul
    5: (128, 0, 128)   # Violeta
}

def pedir_nombre_y_color():
    """Pide al usuario el nombre y el color de la serpiente."""
    nombre = input("Ingresa el nombre de la serpiente: ")
    print("Elige el color de la serpiente:")
    print("1. Rojo")
    print("2. Verde")
    print("3. Celeste")
    print("4. Azul")
    print("5. Violeta")
    color_opcion = int(input("Ingresa el número del color elegido (1-5): "))
    color = colores.get(color_opcion, (0, 255, 0))  # Verde por defecto
    return nombre, color

fps = pygame.time.Clock()

def comida(): #GENERA COMIDA DE FORMA RANDOM POR LA PANTALLA
    random_pos = random.randint(0, 49) * 10
    comida_pos = [random_pos, random_pos]
    return comida_pos

def guardar_puntuacion(nombre, puntaje):
    """Guarda la puntuación en un archivo."""
    with open("puntuaciones.txt", "a") as archivo:
        archivo.write(f"{nombre}: {puntaje}\n")

def obtener_maxima_puntuacion():
    """Obtiene la puntuación máxima del archivo."""
    if not os.path.exists("puntuaciones.txt"):
        return 0
    with open("puntuaciones.txt", "r") as archivo:
        puntuaciones = archivo.readlines()
    max_puntuacion = 0
    for linea in puntuaciones:
        try:
            puntuacion = int(linea.split(": ")[1])
            if puntuacion > max_puntuacion:
                max_puntuacion = puntuacion
        except:
            continue
    return max_puntuacion

# CABEZA DE LA SERPIENTE
def main():
    nombre, color = pedir_nombre_y_color()
    snake_cabeza = [100, 50] # PIXELES DE LA CABEZA DE LA SERPIENTE
    snake_cuerpo = [[100, 50], [90, 50], [80, 50]] # PIXELES DE LA SERPIENTE EN EL CUERPO
    change = "RIGHT"
    run = True
    comida_pos = comida()
    puntaje = 0
    max_puntuacion = obtener_maxima_puntuacion()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN: # Variable que hace que la serpiente se mueva a la derecha cuando mueves el mouse
                if event.key == pygame.K_RIGHT:
                    change = "RIGHT" 
                if event.key == pygame.K_LEFT:
                    change = "LEFT" # Variable que hace que se mueva a la izquierda
                if event.key == pygame.K_UP:
                    change = "UP"
                if event.key == pygame.K_DOWN:
                    change = "DOWN"
        
        # Movimiento de la serpiente
        if change == "RIGHT":
            snake_cabeza[0] += 10
        if change == "LEFT":
            snake_cabeza[0] -= 10
        if change == "UP":
            snake_cabeza[1] -= 10
        if change == "DOWN":
            snake_cabeza[1] += 10
        
        # Actualizar el cuerpo de la serpiente
        snake_cuerpo.insert(0, list(snake_cabeza))
        
        if snake_cabeza == comida_pos: # HACE QUE CUANDO LA CABEZA DE LA SEPIENTE PASE POR UNA COMIDA SUME UN PUNTO
            comida_pos = comida()
            puntaje += 1
            print(puntaje)
        else:
            snake_cuerpo.pop() # HACE QUE LA PARTE DE ATRAS DEL CUERPO DE LA SERPIENTE SE ELIMINE 
        
        # Dibujar la pantalla y la serpiente
        play_surface.fill((0, 0, 0)) # Hace la pantalla negra
        for cabeza in snake_cuerpo:
            pygame.draw.rect(play_surface, color, pygame.Rect(cabeza[0], cabeza[1], 10, 10)) # DIBUJA LA SERPIENTE EN EL COLOR ELEGIDO
            
        texto = fuente_letra.render(f"Puntaje: {puntaje}", 0, (255, 0, 255)) #COLOR DE LA LETRA DEL PUNTAJE
        play_surface.blit(texto, (380, 20)) #POSICIONA EL PUNTAJE ARRIBA A LA DERECHA
        
        texto_max = fuente_letra.render(f"Max: {max_puntuacion}", 0, (255, 255, 0)) #COLOR DE LA LETRA DE LA PUNTUACION MAXIMA
        play_surface.blit(texto_max, (10, 20)) #POSICIONA LA PUNTUACION MAXIMA ARRIBA A LA IZQUIERDA
        
        texto_nombre = fuente_letra.render(f"Jugador: {nombre}", 0, (255, 255, 255)) #COLOR DE LA LETRA DEL NOMBRE
        play_surface.blit(texto_nombre, (10, 50)) #POSICIONA EL NOMBRE DEL JUGADOR ARRIBA A LA IZQUIERDA
        
        if puntaje < 5: #CUANDO EL PUNTAJE SEA MENOR A 5 IRA A VELOCIDAD NORMAL
            fps.tick(30)
        if puntaje >= 10: # CUANDO EL PUNTAJE SEA MAYOR A 10 IRA MAS RAPIDO
            fps.tick(50)
        if puntaje >= 15:
            fps.tick(70) # CUANDO EL PUNTAJE SEA 15 AUMENTA LA VELOCIDAD
        
        if snake_cabeza[0] <= 0 or snake_cabeza[0] >= 500: #SI VAS A LA DERECHA DELTODO PERDES
            run = False
            print("PERDISTE")
        if snake_cabeza[1] <= 0 or snake_cabeza[1] >= 500: #SI VAS A LA IZQUIERDA DELTODO PERDES
            run= False
            print("PERDISTE")
        
        pygame.draw.rect(play_surface, (169, 6, 6), pygame.Rect(comida_pos[0], comida_pos[1], 9, 9)) #DIBUJA LA COMIDA EN ROJO
        pygame.display.flip()
        fps.tick(10)
    
    guardar_puntuacion(nombre, puntaje)
    pygame.quit()
    sys.exit()

main()
