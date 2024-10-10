class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre 
        self.nota = nota  

    def imprimir(self):
        estado = "Aprobado" if self.nota >= 6 else "Reprobado"
        print(f"Nombre: {self.nombre}, Nota: {self.nota}, Estado: {estado}")

alumno1 = Alumno("Juan", 8)
alumno2 = Alumno("Pedro", 4)

alumno1.imprimir_info()
alumno2.imprimir_info()
