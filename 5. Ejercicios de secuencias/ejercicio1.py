def ejercicio1():
    lista = []
    numero = ""
    while numero != 0:
        numero = int(input("Dime un numero: "))
        lista.append(numero)
    
    print(lista)
    lista.sort()
    print(lista)
    lista.reverse()
    print(lista)

def ejercicio2():
    lista = []
    caracter= " "
    while caracter != "":
        caracter = input("Dime un caracter: ")
        lista.append(caracter.lower)
    
    print(lista)
    lista.sort()
    print(lista)
    lista.reverse()
    print(lista)

def ejercicio3():
    palabra = input("Dime una palabra: ")
    if(palabra == palabra[::-1]):
        print("Es palindromo")
    else:
        print("No es palindromo")

def ejercicio4():
    palabra = input("Dime una palabra: ")
    mayusculas = input("Diferenciamos con las mayusculas (Si/No): ")

    if(mayusculas == "Si"):
        if(palabra == palabra[::-1]):
            print("Es palindromo")
        else:
            print("No es palindromo")
    else:
        if(palabra.lower == palabra[::-1].lower):
            print("Es palindromo")
        else:
            print("No es palindromo")

while True:
    print("a) Ejercicio 1")
    print("b) Ejercicio 2")
    print("c) Ejercicio 3")
    print("d) Ejercicio 4")
    print("e) Salir")
    opcion = input("Selecciona una opcion: ")
    
    match opcion:
        case "a":
            ejercicio1()
            break
        case "b":
            ejercicio2()
            break
        case "c":
            ejercicio3()
            break
        case "d":
            ejercicio4()
            break
        case "e":
            exit()

