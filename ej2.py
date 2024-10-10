class Persona:
    def __init__(self, nombre="", edad=0):
        self.nombre = nombre
        self.edad = edad

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_edad(self, edad):
        self.edad = edad

    def get_nombre(self):
        return self.nombre

    def get_edad(self):
        return self.edad

    def print_persona(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")

persona1 = Persona("Juan", 14)
persona2 = Persona("Pedro", 25)

persona1.print_persona()
persona2.print_persona()
