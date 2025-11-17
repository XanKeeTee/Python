class Persona:
    def __init__(self, nombre="", apellidos="", dni="", edad=0):
        """
        Constructor de la clase Persona.
        Utiliza los setters para validar y asignar los datos iniciales.
        """
        self.__nombre = ""
        self.__apellidos = ""
        self.__dni = ""
        self.__edad = 0
        self.set_nombre(nombre)
        self.set_apellidos(apellidos)
        self.set_dni(dni)
        self.set_edad(edad)

    def set_nombre(self, nombre):
        """Valida que el nombre no sea una cadena vacía y lo guarda en mayúsculas."""
        if isinstance(nombre, str) and nombre.strip():
            self.__nombre = nombre.strip().upper()
        else:
            print("Error: El nombre no puede estar vacío.")

    def set_apellidos(self, apellidos):
        """Valida que los apellidos no sean una cadena vacía y los guarda en mayúsculas."""
        if isinstance(apellidos, str) and apellidos.strip():
            self.__apellidos = apellidos.strip().upper()
        else:
            print("Error: Los apellidos no pueden estar vacíos.")

    def set_dni(self, dni):
        """Valida que el DNI no sea una cadena vacía y lo guarda en mayúsculas."""
        if isinstance(dni, str) and dni.strip():
            self.__dni = dni.strip().upper()
        else:
            print("Error: El DNI no puede estar vacío.")

    def set_edad(self, edad):
        """Valida que la edad sea un número entero y positivo."""
        if isinstance(edad, int) and edad >= 0:
            self.__edad = edad
        else:
            print("Error: La edad debe ser un valor entero positivo.")

    # --- Getters ---
    def get_nombre(self):
        return self.__nombre

    def get_apellidos(self):
        return self.__apellidos

    def get_dni(self):
        return self.__dni

    def get_edad(self):
        return self.__edad

    # --- Métodos adicionales ---
    def mostrar(self):
        """Muestra los datos de la persona."""
        print(f"Nombre: {self.__nombre} {self.__apellidos}")
        print(f"DNI: {self.__dni}")
        print(f"Edad: {self.__edad}")

    def mayorDeEdad(self):
        """Devuelve True si la persona es mayor de edad (>= 18), False en caso contrario."""
        return self.__edad >= 18