class Contacto:
    def __init__(self, nombre, telefono, email):
        self.nombre, self.telefono, self.email = nombre, telefono, email
    def __str__(self):
        return f"Nombre: {self.nombre}, Teléfono: {self.telefono}, Email: {self.email}"

class Agenda:
    def __init__(self):
        self.contactos = []
    def agregar(self, contacto):
        self.contactos.append(contacto)
    def mostrar(self):
        print("\n".join(str(c) for c in self.contactos) or "No hay contactos.")

agenda = Agenda()
while True:
    opcion = input("\n1. Agregar contacto\n2. Mostrar contactos\n3. Salir\nOpción: ")
    if opcion == '1':
        datos = [input(f"Ingrese {campo}: ") for campo in ["nombre", "teléfono", "email"]]
        agenda.agregar(Contacto(*datos))
        print(f"Contacto '{datos[0]}' agregado.")
    elif opcion == '2':
        print("Contactos en la agenda:")
        agenda.mostrar()
    elif opcion == '3':
        print("Gracias por usar la agenda.")
        break
    else:
        print("Opción inválida.")
