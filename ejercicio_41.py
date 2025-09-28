class Clase41A:
    def __init__(self, nombre):
        self.nombre = nombre

class Clase41B:
    def __init__(self, dato):
        self.dato = dato

if __name__ == "__main__":
    a = Clase41A("EjemploA")
    b = Clase41B("EjemploB")
    print(a.nombre, b.dato)
