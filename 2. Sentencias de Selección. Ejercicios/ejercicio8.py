# Ejercicio 8 | Miguel Angel Gambero

"""
8. Escribe un programa que recoja un mes del año (en número) y devuelva el
número de días que tiene el mes. En caso de indicar un mes incorrecto deberá
mostrar un mensaje de error.
"""
mes = int(input("Dime un mes del año (1-12): "))
if mes in [1, 3, 5, 7, 8, 10, 12]:
    print("El mes tiene 31 dias")
elif mes in [4, 6, 9, 11]:
    print("El mes tiene 30 dias")
elif mes == 2:
    print("El mes tiene 28 o 29 dias")
else:
    print("Mes incorrecto")