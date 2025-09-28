class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre, self.precio, self.cantidad = nombre, precio, cantidad
    def descuento(self, porcentaje):
        return f"{self.nombre} con {porcentaje}% desc.: ${self.precio*(1-porcentaje/100):.2f}"

    def total(self):
        return f"{self.cantidad} x {self.nombre} = ${self.precio*self.cantidad:.2f}"
p1 = Producto("Laptop", 1500, 2)
p2 = Producto("Smartphone", 800, 3)
for p in (p1, p2):
    print(p.descuento(10 if p.nombre=="Laptop" else 5))
    print(p.total())
