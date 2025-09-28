class Clase50A:
    def __init__(self, nombre):
        self.nombre = nombre

class Clase50B:
    def __init__(self, dato):
        self.dato = dato

if __name__ == "__main__":
    a = Clase50A("EjemploA")
    b = Clase50B("EjemploB")
    print(a.nombre, b.dato)
