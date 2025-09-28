class Clase29A:
    def __init__(self, nombre):
        self.nombre = nombre

class Clase29B:
    def __init__(self, dato):
        self.dato = dato

if __name__ == "__main__":
    a = Clase29A("EjemploA")
    b = Clase29B("EjemploB")
    print(a.nombre, b.dato)
