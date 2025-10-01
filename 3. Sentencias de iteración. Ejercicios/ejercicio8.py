# Ejercicio 7 | Miguel Angel Gambero

"""
8. Escribe un programa que recoja un número y calcule si es primo.
"""
numero = int(input("Introduce un número: "))
es_primo = True

for i in range(2, numero):
    if numero % i == 0:
        es_primo = False
if es_primo and numero > 1:
    print(f"El número {numero} es primo.")
else:
    print(f"El número {numero} no es primo.")
