# Ejercicio 10 | Miguel Angel Gambero

"""
10.Escribe un programa que recoja un número y muestre un triángulo formado por
secuencias decrecientes de números impares. Por ejemplo, si se introduce el
5 se debe mostrar:
1
3 1
5 3 1
7 5 3 1
9 7 5 3 1
"""
numero = int(input("Introduce un número: "))
for i in range(1, numero + 1):
    for j in range(2 * i - 1, 0, -2):
        print(j, end=" ")
    print()