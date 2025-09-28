class Clase46A:
    def __init__(self, nombre):
        self.nombre = nombre

class Clase46B:
    def __init__(self, dato):
        self.dato = dato

if __name__ == "__main__":
    a = Clase46A("EjemploA")
    b = Clase46B("EjemploB")
    print(a.nombre, b.dato)
