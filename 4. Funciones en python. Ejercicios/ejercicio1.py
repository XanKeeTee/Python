import math
import random


def mostrarRombo():
    tamañoRombo = int(input("Digame el tamaño del rombo: "))
    if tamañoRombo % 2 == 0:
        tamañoRombo += 1

    for i in range(tamañoRombo // 2 + 1):
        espacios = " " * (tamañoRombo // 2 - i)
        asteriscos = "*" * (2 * i + 1)
        print(espacios + asteriscos)

    # Parte inferior del rombo
    for i in range(tamañoRombo // 2 - 1, -1, -1):
        espacios = " " * (tamañoRombo // 2 - i)
        asteriscos = "*" * (2 * i + 1)
        print(espacios + asteriscos)

def numeroAleatorio():
    numero = int(random.random()*10)
    return numero

def adivinarNumero(numeroAleatorio):
    numeroUsuario = ""

    while(numeroUsuario!=numeroAleatorio):
        numeroUsuario = int(input("Dime un numero: "))
        if(numeroUsuario == numeroAleatorio):
            print("ACERTASTE EL NUMERO!!")

def ecuacionSegundoGrado():

    a = float(input("Introduce el coeficiente 'a': "))
    b = float(input("Introduce el coeficiente 'b': "))
    c = float(input("Introduce el coeficiente 'c': "))

    delta = (b**2) - (4*a*c)

    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print("Hay dos soluciones reales:")
        print(f"x1 = {x1}")
        print(f"x2 = {x2}")
    elif delta == 0:
        x = -b / (2*a)
        print("Hay una solución real:")
        print(f"x = {x}")
    else:
        print("La ecuación no tiene soluciones reales.")

print("MENÚ DE OPCIONES")
print("a) Mostrar un rombo.")
print("b) Adivinar un número.")
print("c) Resolver una ecuación de segundo grado.")
print("d) Tabla de números.")
print("e) Cálculo del número factorial de un número.")
print("f) Cálculo de un número de la sucesión de Fibonacci.")
print("g) Tabla de multiplicar.")
print("h) Salir")
opcion = str(input("Eliga una opcion: "))

while opcion != ("h"):
    match opcion:
        case "a":
            mostrarRombo()
            break
        case "b":
            adivinarNumero(numeroAleatorio())
            break
        case "c":
            ecuacionSegundoGrado()
            break
