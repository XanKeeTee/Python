"""
Examen Python
Miguel Angel Gambero | 2ºDAW
""" #
def remplazarVocales(palabra):
    newPalabra = ""
    for letra in palabra:
        if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u" or letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U":
            newPalabra += "*"
        else:
            newPalabra += letra
    return newPalabra

def numeroMayorAnterior(cantidadNumeros):
    numeroMayor = 0
    for i in range (1,cantidadNumeros+1):
        numero = int(input("Digame un numero: "))
        if numeroMayor<numero:
            print("El numero introducido: ", numero, " es mayor que el numero anterior : ",numeroMayor)
            numeroMayor = numero
        else:
            print("El numero introducido: ", numero, " no es mayor que el numero anterior : ",numeroMayor)

def palabraLarga(frase):
    arrayPalabras = frase.split(" ")
    palabraMasLarga = ""
    cantidadLetrasPalabraLarga = 0

    for palabra in arrayPalabras:
        cantidadLetra = len(palabra)
        if(cantidadLetra>cantidadLetrasPalabraLarga):
            palabraMasLarga = palabra
            cantidadLetrasPalabraLarga = cantidadLetra
    
    return palabraMasLarga

def rectanguloImpares(fila,columna):
    rectangulo = []
    contador = 99
    for i in range (fila):
        for j in range (columna):
            print(contador, end=" ")
            contador -= 2
            if contador < 1:
                contador = 99
        print()
    print()

def contarPalabras(palabra):
    diccionario = {}
    arrayLetras =[]

    letraMasrepetida = ""
    max = 0
    for letra in palabra:
        diccionario[letra] = 1
        arrayLetras.append(letra)
        for letraArray in arrayLetras:
            if letraArray == letra:
                diccionario[letra] += 1

    for letraDiccionario,cantidad in diccionario.items():
        print("La letra ", letraDiccionario , " repetida ",int(cantidad/2) , " veces")

        if cantidad > max:
            max = cantidad
            letraMasrepetida = letraDiccionario
    
    print("La letra mas repetida es", letraMasrepetida)

while True:
    print("")
    print("a) Reemplazar vocales de una frase")
    print("b) Mensaje cuando el numero introducido no sea mayor que el primero .")
    print("c)Encontrar la primera palabra más larga")
    print("d) Mostrar rectángulo con números impares entre 0 y 100 .")
    print("e) Contar laaparición de cada carácter en una palabra. Mostrar diccionario y el carácter con más apariciones.")
    print("f) Salir")
    opcion = input("Seleccione una opcion: ")

    match opcion:
        case "a":
            palabra = input("Pongame una palabra: ")
            palabraFormateada = remplazarVocales(palabra)
            print(palabraFormateada)
        case "b":
            cantidadNumeros = int(input("Que cantidad de numeros desea introducir: "))
            if cantidadNumeros<=0:
                print("El numero no puede ser igual o menor que 0")
            else:
                numeroMayorAnterior(cantidadNumeros)
        case "c":
            frase = input("Escriba una frase: ")
            print("La palabra mas larga de la frase es :",palabraLarga(frase))
        case "d":
            fila = int(input("Digame la fila: "))
            columna = int(input("Digame la cantidad de columnas: "))
            rectanguloImpares(fila,columna)
        case "e":
            palabra = input("Digame una palabra: ")
            palabra.lower
            print(contarPalabras(palabra))
        case "f":
            print("Saliendo del programa...")
            exit()