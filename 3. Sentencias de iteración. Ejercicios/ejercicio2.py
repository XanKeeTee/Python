# Ejercicio 2 | Miguel Angel Gambero

"""
2. Escribe un programa que recoja un número y calcule su factorial.
"""
numero = int(input("Dime un numero: "))
factorial = 1

for i in range(1, numero + 1):
    factorial *= i

print("El factorial de", numero, "es", factorial)
