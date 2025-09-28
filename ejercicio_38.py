class Clase38A:
    def __init__(self, nombre):
        self.nombre = nombre

class Clase38B:
    def __init__(self, dato):
        self.dato = dato

if __name__ == "__main__":
    a = Clase38A("EjemploA")
    b = Clase38B("EjemploB")
    print(a.nombre, b.dato)
