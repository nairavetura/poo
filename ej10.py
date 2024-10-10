class Cliente:    
    def __init__(self):        
        self.nombre = input("Ingrese el nombre del cliente: ")        
        self.cantidad = 0    

    def extraer(self, cantidad):        
        if cantidad > self.cantidad:
            print("No hay suficiente saldo para realizar la extracción.")
        else:
            self.cantidad -= cantidad    

    def depositar(self, cantidad):        
        if cantidad > 0:
            self.cantidad += cantidad    
        else:
            print("El monto debe ser positivo.")

    def imprimir(self):        
        print("El nombre del cliente es", self.nombre)        
        print("La cantidad total que ha depositado es:", self.cantidad, "pesos")


class Banco:     
    def __init__(self):        
        self.cliente1 = Cliente()        

    def operacion(self):        
        self.cliente1.depositar(1000)
        self.cliente1.extraer(500)        

    def mostrar_total(self):        
        self.cliente1.imprimir()


if __name__ == "__main__":
    banco1 = Banco()
    banco1.operacion()
    banco1.mostrar_total()
