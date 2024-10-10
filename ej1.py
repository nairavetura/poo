class Persona:
    def __init__(self):
        self.nombre = ""
        self.edad = 0

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

persona1 = Persona()
persona1.set_nombre("Juan")
persona1.set_edad(14)

persona2 = Persona()
persona2.set_nombre("Pedro")
persona2.set_edad(25)

persona1.print_persona()
persona2.print_persona()
