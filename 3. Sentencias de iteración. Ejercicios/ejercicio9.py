# Ejercicio 7 | Miguel Angel Gambero

"""
9. Escribe un programa que recoja un número impar. Debe asegurarse de que
sea impar, en caso de no serlo debe descartarlo y pedirlo de nuevo. Una vez
tenga el número impar debe mostrar una pirámide de asteriscos cuya base es
igual al número introducido. Por ejemplo, si se introduce el valor 7 se debe
mostrar:
   *
  ***
 *****
******* <- base de la pirámide (7 asteriscos)
"""
numero = int(input("Introduce un número impar: "))
while numero % 2 == 0:
    numero = int(input("El número no es impar. Introduce un número impar: "))
for i in range(1, numero + 1, 2):
    print(" " * ((numero - i) // 2) + "*" * i)