"""
2. Modificar el programa anterior para que pueda manejar varios nombres.
"""
def mostrarDiccionario(lista_usuarios):
    if not lista_usuarios:
        print("La lista esta vacia")
    else:
        for usuario in lista_usuarios:
            print("Lista\n----------------")
            print(usuario["nombre"]," tiene ",usuario["edad"]," años, vive en ", usuario["direccion"]," y su número de teléfono es ",usuario["telefono"])

def annadirUsuario(lista_usuarios):
    nombre = str(input("Digame su nombre: "))
    edad = int(input("Digame su edad: "))
    direccion = str(input("Digame su direccion: "))
    telefono = input("Digame su numero de telefono: ")

    diccionario = {
        "nombre":nombre,
        "edad":edad,
        "direccion":direccion,
        "telefono":telefono
    }
    lista_usuarios.append(diccionario)

lista_usuarios = []

while True:
    print("\na) Mostrar lista.")
    print("b) Añadir un usuario a la lista.")
    print("h) Salir :")
    opcion = input("Selecciona una opcion: \n")

    match opcion:
        case "a":
            mostrarDiccionario(lista_usuarios)
        case "b":
            annadirUsuario(lista_usuarios)
        case "h":
            exit()