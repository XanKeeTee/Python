"""
1. Escribir un programa que pregunte al usuario su nombre, edad,
dirección y teléfono y lo guarde en un diccionario. Después debe
mostrar por pantalla el mensaje <nombre> tiene <edad> años,
vive en <dirección> y su número de teléfono es
<teléfono>.
"""
diccionario = {}

diccionario["nombre"] = str(input("Digame su nombre: "))
diccionario["edad"] = int(input("Digame su edad: "))
diccionario["direccion"] = str(input("Digame su direccion: "))
diccionario["telefono"] = input("Digame su numero de telefono: ")

print(diccionario["nombre"]," tiene ",diccionario["edad"]," años, vive en ", diccionario["direccion"]," y su número de teléfono es ",diccionario["telefono"]