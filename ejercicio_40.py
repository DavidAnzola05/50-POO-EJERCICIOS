class Clase40A:
    def __init__(self, nombre):
        self.nombre = nombre

class Clase40B:
    def __init__(self, dato):
        self.dato = dato

if __name__ == "__main__":
    a = Clase40A("EjemploA")
    b = Clase40B("EjemploB")
    print(a.nombre, b.dato)
