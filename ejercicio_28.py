from datetime import date, timedelta

class Libro:
    def __init__(self, titulo):
        self.titulo = titulo
        self.disponible = True

class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.prestamos = []

class Prestamo:
    def __init__(self, libro, usuario, dias=7):
        self.libro = libro
        self.usuario = usuario
        self.fecha_inicio = date.today()
        self.fecha_vencimiento = self.fecha_inicio + timedelta(days=dias)
        libro.disponible = False
        usuario.prestamos.append(self)

    def multa(self):
        hoy = date.today()
        if hoy > self.fecha_vencimiento:
            return (hoy - self.fecha_vencimiento).days * 2
        return 0


if __name__ == "__main__":
    l = Libro("1984")
    u = Usuario("Mateo")
    p = Prestamo(l, u, dias=3)
    print("Libro:", l.titulo, "Prestado a:", u.nombre)
    print("Vence el:", p.fecha_vencimiento)
    print("Multa actual:", p.multa())
