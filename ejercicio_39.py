class Clase39A:
    def __init__(self, nombre):
        self.nombre = nombre

class Clase39B:
    def __init__(self, dato):
        self.dato = dato

if __name__ == "__main__":
    a = Clase39A("EjemploA")
    b = Clase39B("EjemploB")
    print(a.nombre, b.dato)
