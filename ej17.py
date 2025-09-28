VALOR_HORA = 6471

class Empleado:
    def __init__(self, nombre, horas, extra=""):
        self.nombre, self.horas, self.salario, self.extra = nombre, horas, horas*VALOR_HORA, extra
    def detalles(self):
        return f"Empleado: {self.nombre}, Salario: {self.salario} {self.extra}"

op = input("1. Tiempo completo\n2. Medio tiempo\nOpción: ")
nombre = input("Nombre: ")
horas = int(input("Horas trabajadas al mes: "))
extra = f"Beneficios: {input('Beneficios: ')}" if op=="1" else f"Horas: {horas}"
print(Empleado(nombre, horas, extra).detalles())
