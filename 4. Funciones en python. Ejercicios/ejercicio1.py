import math
import random


def mostrarRombo(tamañoRombo):
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
    numero = int(random.random()*100)
    return numero

def adivinarNumeroAleatiro(numeroAleatorio,numeroUsuario):
        if numeroUsuario == numeroRandom:
            return True
        else: 
            return False

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
            tamañoRombo = int(input("Digame el tamaño del rombo: "))
            mostrarRombo(tamañoRombo)
            break
        case "b":
            condicion = True
            while condicion:
                numeroRandom = numeroAleatorio()
                numeroUsuario = int(input("Digame un numero: "))

                condicion = adivinarNumeroAleatiro(numeroRandom,numeroUsuario)

                while condicion:
                    numero

                

            
