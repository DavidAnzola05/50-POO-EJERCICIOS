class Clase43A:
    def __init__(self, nombre):
        self.nombre = nombre

class Clase43B:
    def __init__(self, dato):
        self.dato = dato

if __name__ == "__main__":
    a = Clase43A("EjemploA")
    b = Clase43B("EjemploB")
    print(a.nombre, b.dato)
