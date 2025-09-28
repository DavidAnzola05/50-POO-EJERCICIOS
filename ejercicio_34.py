class Clase34A:
    def __init__(self, nombre):
        self.nombre = nombre

class Clase34B:
    def __init__(self, dato):
        self.dato = dato

if __name__ == "__main__":
    a = Clase34A("EjemploA")
    b = Clase34B("EjemploB")
    print(a.nombre, b.dato)
