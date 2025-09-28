class Clase48A:
    def __init__(self, nombre):
        self.nombre = nombre

class Clase48B:
    def __init__(self, dato):
        self.dato = dato

if __name__ == "__main__":
    a = Clase48A("EjemploA")
    b = Clase48B("EjemploB")
    print(a.nombre, b.dato)
