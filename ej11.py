class Reloj:
    def __init__(self, h=0, m=0, s=0):
        self.h, self.m, self.s = h, m, s

    def ajustar(self, h, m, s):
        self.h, self.m, self.s = h, m, s

    def avanzar(self):
        self.s += 1
        if self.s == 60:
            self.s, self.m = 0, self.m + 1
            if self.m == 60:
                self.m, self.h = 0, self.h + 1
                if self.h == 24:
                    self.h = 0

    def mostrar(self):
        return f"{self.h:02}:{self.m:02}:{self.s:02}"

reloj = Reloj(23, 59, 58)
print("Reloj digital:", reloj.mostrar())

op = input("\n1. Ajustar hora\n2. Ver formato 24 horas\nOpción: ")
if op == '1':
    h = int(input("Horas (0-23): "))
    m = int(input("Minutos (0-59): "))
    s = int(input("Segundos (0-59): "))
    reloj.ajustar(h, m, s)
    print("Hora ajustada:", reloj.mostrar())
elif op == '2':
    print("Hora en formato 24 horas:", reloj.mostrar())
else:
    print("Opción inválida.")
