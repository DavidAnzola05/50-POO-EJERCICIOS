class Clase31A:
    def __init__(self, nombre):
        self.nombre = nombre

class Clase31B:
    def __init__(self, dato):
        self.dato = dato

if __name__ == "__main__":
    a = Clase31A("EjemploA")
    b = Clase31B("EjemploB")
    print(a.nombre, b.dato)
