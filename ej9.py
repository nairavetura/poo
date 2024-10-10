class Agenda:
    def __init__(self):
        self.contactos = []

    def menu(self):
        while True:
            print("\n--- Menu de la Agenda ---")
            print("1. Añadir contacto")
            print("2. Listar contactos")
            print("3. Buscar contacto")
            print("4. Editar contacto")
            print("5. Cerrar agenda")
            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                self.agregar_contacto()
            elif opcion == '2':
                self.listar_contactos()
            elif opcion == '3':
                self.buscar_contacto()
            elif opcion == '4':
                self.editar_contacto()
            elif opcion == '5':
                print("Cerrando agenda...")
                break
            else:
                print("Opción no válida. Intente de nuevo.")

    def agregar_contacto(self):
        nombre = input("Introduzca el nombre: ")
        telefono = input("Introduzca el teléfono: ")
        email = input("Introduzca el e-mail: ")
        self.contactos.append({'nombre': nombre, 'telefono': telefono, 'email': email})
        print("Contacto agregado con éxito.")

    def listar_contactos(self):
        print("\n--- Lista de Contactos ---")
        if not self.contactos:
            print("No hay contactos en la agenda.")
            return
        for idx, contacto in enumerate(self.contactos, start=1):
            print(f"{idx}. Nombre: {contacto['nombre']}, Teléfono: {contacto['telefono']}, Email: {contacto['email']}")

    def buscar_contacto(self):
        print("---------------------")
        print("Buscador de contactos")
        print("---------------------")
        nom = input("Introduzca el nombre del contacto: ")
        for contacto in self.contactos:
            if contacto['nombre'].lower() == nom.lower():
                print("Datos del contacto:")
                print(f"Nombre: {contacto['nombre']}")
                print(f"Teléfono: {contacto['telefono']}")
                print(f"E-mail: {contacto['email']}")
                return
        print("Contacto no encontrado.")

    def editar_contacto(self):
        print("---------------")
        print("Editar contacto")
        print("---------------")
        nom = input("Introduzca el nombre del contacto a editar: ")
        for contacto in self.contactos:
            if contacto['nombre'].lower() == nom.lower():
                print("Selecciona qué quieres editar:")
                print("1. Nombre")
                print("2. Teléfono")
                print("3. E-mail")
                opcion = input("Introduzca la opción deseada: ")
                
                if opcion == '1':
                    nuevo_nombre = input("Introduzca el nuevo nombre: ")
                    contacto['nombre'] = nuevo_nombre
                elif opcion == '2':
                    nuevo_telefono = input("Introduzca el nuevo teléfono: ")
                    contacto['telefono'] = nuevo_telefono
                elif opcion == '3':
                    nuevo_email = input("Introduzca el nuevo e-mail: ")
                    contacto['email'] = nuevo_email
                else:
                    print("Opción no válida.")
                print("Contacto actualizado con éxito.")
                return
        print("Contacto no encontrado.")

if __name__ == "__main__":
    agenda = Agenda()
    agenda.menu()
