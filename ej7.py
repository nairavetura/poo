class Triangulo:
    def __init__(self):        
        self.lado1 = int(input("\nIngrese el valor del primer lado: "))        
        self.lado2 = int(input("Ingrese el valor del segundo lado: "))        
        self.lado3 = int(input("Ingrese el valor del tercer lado: "))   

    def mostrar(self):
        print("Los lados del triángulo son:")  
        print(self.lado1)        
        print(self.lado2)       
        print(self.lado3)        

    def tipo_triangulo(self):        
        if self.lado1 == self.lado2 == self.lado3:
            print("El triángulo es equilátero")        
        elif self.lado1 != self.lado2 and self.lado2 != self.lado3 and self.lado1 != self.lado3:
            print("El triángulo es escaleno")        
        else:            
            print("El triángulo es isósceles")

triangulo1 = Triangulo()
triangulo1.mostrar()
triangulo1.tipo_triangulo()
print("")
