import random

class Dado:
    def __init__(self, caras): self.caras = caras
    def lanzar(self): return random.randint(1, self.caras)
    def estadisticas(self, n):
        return {i: [self.lanzar() for _ in range(n)].count(i) for i in range(1, self.caras+1)}

caras = int(input("Número de caras: "))
n = int(input("Número de lanzamientos: "))
dado = Dado(caras)
for cara, freq in dado.estadisticas(n).items():
    print(f"Cara {cara}: {freq}")
