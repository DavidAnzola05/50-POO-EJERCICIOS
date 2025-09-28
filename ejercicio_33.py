class Clase33A:
    def __init__(self, nombre):
        self.nombre = nombre

class Clase33B:
    def __init__(self, dato):
        self.dato = dato

if __name__ == "__main__":
    a = Clase33A("EjemploA")
    b = Clase33B("EjemploB")
    print(a.nombre, b.dato)
