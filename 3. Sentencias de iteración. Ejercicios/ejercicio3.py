# Ejercicio 2 | Miguel Angel Gambero

"""
3. Escribe un programa que recoja números por teclado hasta que se introduzca
el valor cero. A continuación, debe mostrar el número de valores introducidos,
el valor mínimo introducido, el máximo, la suma de todos ellos y su media
aritmética (todos los cálculos sin contar el cero)
"""
numero = int(input("Dime un numero (0 para salir): "))

contador = 0
suma = 0
minimo = None
maximo = None

while numero != 0:
    contador += 1
    suma += numero
    if minimo is None or numero < minimo:
        minimo = numero
    if maximo is None or numero > maximo:
        maximo = numero
    numero = int(input("Dime un numero (0 para salir): "))
if contador > 0:
    media = suma / contador
    print("Has introducido", contador, "numeros")
    print("El minimo es", minimo)
    print("El maximo es", maximo)
    print("La suma es", suma)
    print("La media es", media)
else:
    print("No has introducido ningun numero")
