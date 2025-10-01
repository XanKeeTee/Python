# Ejercicio 2 | Miguel Angel Gambero

"""
2. Escribe un programa que recoja un número por teclado y muestre el día de la
semana que es (1 = Lunes, 2 = Martes...). En caso de introducir un número
incorrecto, mostrará el mensaje “Día de la semana incorrecto”.
"""

numero = int(input("Digame un numero: "))

match numero:
    case 1:
        print("Es lunes")
    case 2:
        print("Es martes")
    case 3:
        print("Es miercoles")
    case 4:
        print("Es jueves")
    case 5:
        print("Es viernes")
    case 6:
        print("Es sabado")
    case 7:
        print("Es domingo")
    case _:
        print("No equivale a ningun dia de la semana")