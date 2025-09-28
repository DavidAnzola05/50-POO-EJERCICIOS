class Clase44A:
    def __init__(self, nombre):
        self.nombre = nombre

class Clase44B:
    def __init__(self, dato):
        self.dato = dato

if __name__ == "__main__":
    a = Clase44A("EjemploA")
    b = Clase44B("EjemploB")
    print(a.nombre, b.dato)
