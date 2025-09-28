class Clase47A:
    def __init__(self, nombre):
        self.nombre = nombre

class Clase47B:
    def __init__(self, dato):
        self.dato = dato

if __name__ == "__main__":
    a = Clase47A("EjemploA")
    b = Clase47B("EjemploB")
    print(a.nombre, b.dato)
