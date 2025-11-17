class Persona:
    def __init__(self,nombre,direccion,telefono):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono
    

    def getNombre(self):
        return self.__nombre
    
    def getDireccion(self):
        return self.__direccion
    
    def getTelefono(self):
        return self.__telefono

    def setDireccion(self,direccion):
        self.__direccion = direccion
    
    def setTelefono(self,telefono):
        self.__telefono = telefono
    
    def mostrarPersona(self):
        print("Nombre: ",self.__nombre,"| Direccion: ",self.__direccion,"| Telefono: ",self.__telefono)

def annadirAgenda(agenda, persona):
    if persona.getNombre() in agenda:
        print("Error: Ya existe un contacto con ese nombre.")
    else:
        agenda[persona.getNombre()] = persona
        print("Contacto añadido correctamente.")

def mostrarAgenda(agenda):
    if not agenda:
        print("La agenda esta vacia")
    else:
        for nombre in sorted(agenda.keys()):
            agenda[nombre].mostrarPersona()

def modificarContacto(agenda, nombre_usuario):
    if nombre_usuario in agenda:
        print("Usuario encontrado. Introduce los nuevos datos.")
        persona = agenda[nombre_usuario]
        direccion_nueva = input("Digame la nueva direccion: ")
        persona.setDireccion(direccion_nueva)
        telefono_nuevo = input("Digame el nuevo telefono: ")
        persona.setTelefono(telefono_nuevo)
        print("Contacto modificado correctamente.")
    else:
        print("El usuario no existe.")

def buscarTelefono(agenda,nombre_usuario):
    if nombre_usuario in agenda:
        print("El telefono es:",agenda[nombre_usuario].getTelefono())
    else:
        print("El nombre no existe.")
    
def eliminarContacto(agenda,nombre_usuario):
    if nombre_usuario in agenda:
        del agenda[nombre_usuario]
        print("Contacto eliminado correctamente.")
    else:
        print("El contacto no existe.")

agenda = {} 
while True:
    print("""MENÚ DE OPCIONES
    a) Listado de contactos por orden alfabético.
    b) Añadir un nuevo contacto.
    c) Modificar un contacto.
    d) Buscar un número de teléfono.
    e) Eliminar un contacto.
    f) Salir""")
    opcion = input("Seleccione una opcion: ")

    match(opcion):
        case "a":
            mostrarAgenda(agenda)
        case "b":
            nombre = input("Digame un nombre: ")
            direccion = input("Digame la direccion: ")
            telefono = input("Digame su telefono: ")
            annadirAgenda(agenda, Persona(nombre,direccion,telefono))
        case "c":
            nombre = input("Digame el nombre de la persona: ")
            modificarContacto(agenda,nombre)
        case "d":
            nombre = input("Digame el nombre de la persona: ")
            buscarTelefono(agenda,nombre)
        case "e":
            nombre = input("Digame el nombre del contacto a eliminar: ")
            eliminarContacto(agenda, nombre)
        case "f":
            print("Saliendo del programa...")
            break
        case _:
            print("Opción no válida.")