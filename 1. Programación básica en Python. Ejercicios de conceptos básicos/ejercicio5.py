# Ejercicio 5 | Miguel Angel Gambero

"""
5. Escribe un programa que recoja un número y muestre su valor absoluto.
"""
num = float(input("Dame un numero: "))
if num < 0:
    num = -num
print("El valor absoluto del numero es: ", num)