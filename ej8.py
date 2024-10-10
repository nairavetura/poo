class Calculadora:
    def __init__(self):        
        self.num1 = int(input("\nIngrese el primer número: "))        
        self.num2 = int(input("Ingrese el segundo número: "))   
            
    def suma(self):
        print("La suma es:", self.num1 + self.num2)       
        
    def resta(self):
        print("La resta es:", self.num1 - self.num2)   
             
    def multiplicacion(self):
        print("La multiplicación es:", self.num1 * self.num2)  
          
    def division(self):       
        if self.num2 == 0:            
            print("PARA LA DIVISIÓN")            
            print("El segundo número debe ser diferente de 0")       
        else:            
            print("La división es:", self.num1 / self.num2)

calculadora1 = Calculadora()
calculadora1.suma()
calculadora1.resta()
calculadora1.multiplicacion()
calculadora1.division()
print("")
