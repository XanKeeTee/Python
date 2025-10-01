
def calcularPrecio(edad):
    if edad<5:
        return ("El precio es gratuito")
    elif edad>5 and edad<18:
        return ("El precio es de 3€")
    elif edad>=18 and edad<65:
        return ("El precio es de 6€")
    elif edad>=65:
        return ("El precio es gratuito")

edad = int(input("Digame su edad: "))

print (calcularPrecio(edad))