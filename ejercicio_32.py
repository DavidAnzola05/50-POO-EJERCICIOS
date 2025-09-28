class Clase32A:
    def __init__(self, nombre):
        self.nombre = nombre

class Clase32B:
    def __init__(self, dato):
        self.dato = dato

if __name__ == "__main__":
    a = Clase32A("EjemploA")
    b = Clase32B("EjemploB")
    print(a.nombre, b.dato)
