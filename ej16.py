class Vehiculo:
    def __init__(self, marca, modelo, extra=""):
        self.marca, self.modelo, self.extra = marca, modelo, extra
    def mostrar_info(self):
        print(f"{self.__class__.__name__}: {self.marca} {self.modelo} {self.extra}")

class Carro(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo, f"- Puertas: {puertas}")

class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, cilindraje):
        super().__init__(marca, modelo, f"- Cilindraje: {cilindraje}cc")

class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo, f"- Tipo: {tipo}")

vehiculos = [
    Carro("Toyota", "Corolla", 4),
    Motocicleta("Yamaha", "YZF-R3", 321),
    Bicicleta("Giant", "Escape 3", "Urbana")
]

for v in vehiculos: v.mostrar_info()
