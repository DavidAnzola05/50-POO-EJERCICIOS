class Clase45A:
    def __init__(self, nombre):
        self.nombre = nombre

class Clase45B:
    def __init__(self, dato):
        self.dato = dato

if __name__ == "__main__":
    a = Clase45A("EjemploA")
    b = Clase45B("EjemploB")
    print(a.nombre, b.dato)
