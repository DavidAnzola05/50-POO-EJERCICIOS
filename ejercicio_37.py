class Clase37A:
    def __init__(self, nombre):
        self.nombre = nombre

class Clase37B:
    def __init__(self, dato):
        self.dato = dato

if __name__ == "__main__":
    a = Clase37A("EjemploA")
    b = Clase37B("EjemploB")
    print(a.nombre, b.dato)
