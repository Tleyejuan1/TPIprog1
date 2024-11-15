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

# Función principal del juego
def juego_memoria():
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

# Iniciar el juego
if __name__ == "__main__":
    juego_memoria()

