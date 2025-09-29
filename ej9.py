class Circulo:
    def __init__(self, r): self.r = r
    def area(self): return 3.1416 * self.r**2
    def circunferencia(self): return 2 * 3.1416 * self.r
    def comparar(self, otro):
        return ("El primer círculo es más grande." if self.r > otro.r else
               "El segundo círculo es más grande." if self.r < otro.r else
               "Ambos círculos son del mismo tamaño.")

r1, r2 = float(input("Radio 1: ")), float(input("Radio 2: "))
c1, c2 = Circulo(r1), Circulo(r2)

print(f"Área 1: {c1.area()}, Circunf.: {c1.circunferencia()}")
print(f"Área 2: {c2.area()}, Circunf.: {c2.circunferencia()}")
print(c1.comparar(c2))
