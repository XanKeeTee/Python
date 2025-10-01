# Ejercicio 7 | Miguel Angel Gambero

"""
7. Escribe un programa que recoja una cadena de texto por teclado y una letra a
buscar. Luego debe buscar dicha letra por la cadena y al finalizar debe indicar
el número de veces que se repite la letra en el texto.
"""

texto = input("Introduce una cadena de texto: ")
letra = input("Introduce una letra a buscar: ")
contador = 0
for caracter in texto:
    if caracter == letra:
        contador += 1
print(f"La letra '{letra}' se repite {contador} veces en el texto.")

