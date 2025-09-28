class Clase36A:
    def __init__(self, nombre):
        self.nombre = nombre

class Clase36B:
    def __init__(self, dato):
        self.dato = dato

if __name__ == "__main__":
    a = Clase36A("EjemploA")
    b = Clase36B("EjemploB")
    print(a.nombre, b.dato)
