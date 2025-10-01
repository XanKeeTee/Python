# Ejercicio 3 | Miguel Angel Gambero

"""
3. Escribe un programa que lea tres números y que muestre los números mayor
y menor.
"""
numero1 = int(input("Dime el primer numero: "))
numero2 = int(input("Digame el segundo numero: "))
numero3 = int(input("Digame el tercer numero: "))

max=max(numero1,numero2,numero3)
min=min(numero1,numero2,numero3)

print("El numero mayor es el ",max)
print("El numero menor es el ",min)