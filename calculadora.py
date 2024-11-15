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
    
def raiz(a):
    return a**0.5

def potencia(a, b):
    return a**b
    

print('''Elija la operacion que desea realizar: 
1. Suma.
2. Resta.
3. Multiplicacion.
4. Division.
5. Radicacion.
6. Potenciacion.
7. Salir del programa.''')

opcion = 0

while opcion != 7:

    opcion = int(input("Ingrese numero de la opcion: "))
    if opcion == 7:
        print("Fin del programa.")
    
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
