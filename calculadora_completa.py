# FUNCIONES DE LAS OPERACIONES BASICAS
def suma(a ,b):
    return a + b
def resta(a ,b):
    return a - b
def multiplicacion(a ,b):
    return a * b
def division(a ,b):
    if b != 0:
        return a / b
    else:
        return "Error: Division por cero."
def raiz(indice, radicando):   #primer parametro indice, segundo parametri radicando (indice √ radicando)
    if radicando < 0 and indice % 2 == 0:
        return "Error: No se puede calcular la raíz de un número negativo con un índice par"
    
    resultado = radicando ** (1 / indice)
    return resultado
def potencia(a, b):
    return a**b


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
        return (valor - 32) * 5/9  
    elif tipo_conversion == 2:  # Celsius a Fahrenheit
        return (valor * 9/5) + 32  
    else:
        return "Opción de conversión inválida"
    

# FUNCION LINEAL
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


# MENU PRINCIPAL DE LA CALCULADORA
opcion_principal = 0

while opcion_principal != 4:

    if opcion_principal != 4:
        print('''CALCULADORA MULTIUSOS
        1. Operaciones basicas.
        2. Conversor de unidades.
        3. Calculadora de funcion lienal.
        4. Volver al menu principal del programa.''')
        opcion_principal = int(input("Selecciones una opcion: "))


        if opcion_principal == 1:
            # CUANDO INGRESA OPCION 1:
            print('''Elija la operacion que desea realizar: 
            1. Suma.
            2. Resta.
            3. Multiplicacion.
            4. Division.
            5. Radicacion.
            6. Potenciacion.
            7. Volver al menú principal de la calculadora.''')
            opcion = 0
            while opcion != 7:

                opcion = int(input("Ingrese numero de la opcion: "))
                if opcion == 7:
                    print("Menú principal de la calculadora.")
                
                if opcion != 7:
                    if opcion == 1:
                        num1 = float(input("Ingrese el primer numero: "))
                        num2 = float(input("Ingrese el segundo numero: "))
                        print(suma(num1, num2))
                    elif opcion == 2:
                        num1 = float(input("Ingrese el primer numero: "))
                        num2 = float(input("Ingrese el segundo numero: "))
                        print(resta(num1, num2))
                    elif opcion == 3:
                        num1 = float(input("Ingrese el primer numero: "))
                        num2 = float(input("Ingrese el segundo numero: "))
                        print(multiplicacion(num1, num2))
                    elif opcion == 4:
                        num1 = float(input("Ingrese el primer numero: "))
                        num2 = float(input("Ingrese el segundo numero: "))
                        print(division(num1, num2))
                    elif opcion == 5:
                        num1 = float(input("Ingrese un numero para calcular su raiz cuadrada: "))
                        print(raiz(num1))
                    elif opcion == 6:
                        num1 = float(input("Ingrese la base: "))
                        num2 = float(input("Ingrese el exponente: "))
                        print(potencia(num1, num2))
                    else:
                        print("Opcion invalida.")

        elif opcion_principal == 2:
            




        



