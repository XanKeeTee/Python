# Ejercicio 7 | Miguel Angel Gambero

"""
7.Escribe un programa que recoja la hora del día y devuelva un saludo, según
las siguientes reglas:
    INTERVALO DE HORAS SALUDO
        [7,12) Buenos días
        [12, 20) Buenas tardes
        En otro caso Buenas noches
"""
hora = int(input("Dime la hora del dia (0-23): "))

if 7 <= hora < 12:
    print("Buenos dias")
elif 12 <= hora < 20:
    print("Buenas tardes")
else:
    print("Buenas noches")
