def mostrarLista(contactos):
    if not contactos:
        print("La lista de contactos esta vacia")
    else:
        for nombre,telefono in contactos.items():
            print("Nombre: ",nombre," - Telefono: ",telefono)

def mostarNomreAlfabeticamente(contactos):
    if not contactos:
        print("La lista de contactos esta vacia")
    else:
        for nombre,telefono in sorted(contactos.items()):
            print("Nombre: ",nombre, " - Telefono: ",telefono)

def añadirContacto(contactos):
    nombre = input("Introduzca su nombre: ")
    telefono = input("Introduzca su numero de telefono: ")
    if nombre in contactos or telefono in contactos:
        print("El nombre o el numero de telefono esta en la lista de contactos")
    else:
        contactos[nombre] = telefono

def modificarTelefono(contactos):
    nombreInput = input("Introduzca el nombre del telefono que quieres cambiar: ")
    if nombreInput in contactos:
        print("El nombre introducido esta en la lista.")
        telefono = input("Introducta el telefono: ")
        contactos[nombreInput] = telefono
    else:
        print("El nombre no esta en la lista")

def buscarContacto(contactos):
    telefonoInput = input("Introduzca un numero de telefono: ")
    encontrado = False

    for nombre,telefono in contactos.items():
        if telefono == telefonoInput:
            print("Nombre: ",nombre, " - Telefono: ",telefono)
            encontrado = True
    if not encontrado:
        print("No se ha encontrado el numero de telefono")

def borrarContactos(contatos):
    nombre = input("Nombre del contacto que quiera borrar: ")
    if nombre in contactos:
        del contactos[nombre]
    else:
        print("El nombre no se ha encontrado en la lista")

def borrarLista(contactos):
    confirmacion = input("Quieres borrar la lista?(s/n): ")
    if confirmacion == "s":
        contactos.clear()
        print("Has borrado la lista.")
    else:
        print("La lista no ha sido borrada.")
contactos = {
    "Ana": "654321987",
    "Luis": "612345678",
    "María": "678901234",
    "Pedro": "600112233"
}

while True:
    print("\na) Listado de teléfonos, usando el orden por defecto.")
    print("b) Listado de teléfonos por orden alfabético.")
    print("c) Añadir un nuevo contacto.")
    print("d) Modificar el teléfono de un contacto.")
    print("e) Buscar un número de teléfono.")
    print("f) Eliminar un contacto.")
    print("g) Borrar el listín telefónico.")
    print("h) Salir :")
    opcion = input("Selecciona una opcion: \n")

    match opcion:
        case "a":
            mostrarLista(contactos)
        case "b":
            mostarNomreAlfabeticamente(contactos)
        case "c":
            añadirContacto(contactos)
        case "d":
            modificarTelefono(contactos)
        case "e":
            buscarContacto(contactos)
        case "f":
            borrarContactos(contactos)
        case "g":
            borrarLista(contactos)
        case "h":
            exit()