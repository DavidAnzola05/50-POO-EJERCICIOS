class Clase30A:
    def __init__(self, nombre):
        self.nombre = nombre

class Clase30B:
    def __init__(self, dato):
        self.dato = dato

if __name__ == "__main__":
    a = Clase30A("EjemploA")
    b = Clase30B("EjemploB")
    print(a.nombre, b.dato)
