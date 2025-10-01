def calcularNotaFinal(nota):
    if nota<5:
        return("Estas suspenso")
    elif nota==5:
        return("Tienes un suficiente")
    elif nota==6:
        return("Tienes un bien")
    elif nota==7 or nota==8:
        return("Tienes un notable")
    elif nota==9 or nota == 10:
        return("Tienes un sobresaliente")
    else:
        return("El valor no es valido")

nota = int(input("Dime la nota: "))
print(calcularNotaFinal(nota))

