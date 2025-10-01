# Ejercicio 6 | Miguel Angel Gambero

"""
6. Escribe un programa que recoja las notas de las tres evaluaciones de un
alumno. A continuación debe calcular y mostrar la nota final, teniendo en
cuenta que la primera evaluación cuenta un 20% de la nota final, la segunda
evaluación un 35% y la tercera evaluación un 45%.
"""
eval1 = float(input("Dame la nota de la primera evaluacion: "))
eval2 = float(input("Dame la nota de la segunda evaluacion: "))
eval3 = float(input("Dame la nota de la tercera evaluacion: "))
nota_final = eval1 * 0.2 + eval2 * 0.35 + eval3 * 0.45
print("La nota final del alumno es de: ", nota_final)
