class Rectangulo:
    def __init__(self, base, altura):
        self.base, self.altura = base, altura
    def area(self): return self.base * self.altura
    def perimetro(self): return 2 * (self.base + self.altura)
    def es_cuadrado(self): return self.base == self.altura

b = float(input("Ingrese la base: "))
h = float(input("Ingrese la altura: "))
r = Rectangulo(b, h)

print(f"Área: {r.area()}")
print(f"Perímetro: {r.perimetro()}")
print("Es un cuadrado" if r.es_cuadrado() else "No es un cuadrado")
