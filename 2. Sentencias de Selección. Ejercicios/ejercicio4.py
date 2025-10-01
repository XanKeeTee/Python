# Ejercicio 3 | Miguel Angel Gambero

"""
4. Escribe un programa que recoja dividendo y divisor, y realice su división
siempre que el divisor sea distinto de cero.
"""
dividendo = int(input("Digame el dividendo: "))
divisor = int(input("Digame el divisor: "))
if divisor == 0:
    print ("El divisor no puede ser 0")
else: 
    resultado = dividendo/divisor
    print("El resultado de la division es de ", resultado)