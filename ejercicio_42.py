class Clase42A:
    def __init__(self, nombre):
        self.nombre = nombre

class Clase42B:
    def __init__(self, dato):
        self.dato = dato

if __name__ == "__main__":
    a = Clase42A("EjemploA")
    b = Clase42B("EjemploB")
    print(a.nombre, b.dato)
