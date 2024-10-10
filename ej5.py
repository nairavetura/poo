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

    def es_mayor_de_edad(self):
        return self.edad >= 18

    def es_mayor_que(self, otra_persona):
        return self.edad > otra_persona.get_edad()

    def print_persona(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Mayor de edad: {self.es_mayor_de_edad()}")

    @staticmethod
    def get_mayor(persona1, persona2):
        return persona1 if persona1.get_edad() > persona2.get_edad() else persona2

persona1 = Persona("Juan", 14)
persona2 = Persona("Pedro", 25)

persona1.print_persona()
persona2.print_persona()

if persona1.es_mayor_que(persona2):
    print(f"{persona1.get_nombre()} es mayor que {persona2.get_nombre()}.")
else:
    print(f"{persona1.get_nombre()} no es mayor que {persona2.get_nombre()}.")

mayor = Persona.get_mayor(persona1, persona2)
print(f"La persona de mayor edad es: {mayor.get_nombre()} con {mayor.get_edad()} años.")
