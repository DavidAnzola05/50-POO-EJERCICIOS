class Temperatura:
    def __init__(self, c): self.c = c
    def f(self): return self.c*9/5+32
    def k(self): return self.c+273.15

c = float(input("Ingrese la temperatura en Celsius: "))
t = Temperatura(c)

op = input("1. Celsius a Fahrenheit\n2. Celsius a Kelvin\nOpción: ")
print(f"{t.c}°C son {t.f()}°F") if op=="1" else print(f"{t.c}°C son {t.k()}K")
