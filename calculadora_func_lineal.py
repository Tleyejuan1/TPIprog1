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

