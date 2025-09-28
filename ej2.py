class Calculadora:
    def __init__(self, a, b): self.a, self.b = a, b
    def operar(self, op):
        ops = {
            "1": ("suma", self.a + self.b),
            "2": ("resta", self.a - self.b),
            "3": ("multiplicación", self.a * self.b),
            "4": ("división", self.a / self.b if self.b else "Error: división por cero")
        }
        print(f"Resultado de la {ops[op][0]}: {ops[op][1]}")

a = float(input("Primer número: "))
b = float(input("Segundo número: "))
op = input("1.Sumar  2.Restar  3.Multiplicar  4.Dividir\nOpción: ")
Calculadora(a,b).operar(op)
