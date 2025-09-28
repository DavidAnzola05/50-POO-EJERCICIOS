class Clase49A:
    def __init__(self, nombre):
        self.nombre = nombre

class Clase49B:
    def __init__(self, dato):
        self.dato = dato

if __name__ == "__main__":
    a = Clase49A("EjemploA")
    b = Clase49B("EjemploB")
    print(a.nombre, b.dato)
