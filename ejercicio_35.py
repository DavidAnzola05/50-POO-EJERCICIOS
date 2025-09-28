class Clase35A:
    def __init__(self, nombre):
        self.nombre = nombre

class Clase35B:
    def __init__(self, dato):
        self.dato = dato

if __name__ == "__main__":
    a = Clase35A("EjemploA")
    b = Clase35B("EjemploB")
    print(a.nombre, b.dato)
