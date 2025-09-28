class Libro:
    def __init__(self, titulo, autor, estado="disponible"):
        self.titulo, self.autor, self.estado = titulo, autor, estado
    def prestar(self): self.estado = "prestado" if self.estado=="disponible" else self.estado
    def devolver(self): self.estado = "disponible" if self.estado=="prestado" else self.estado
    def mostrar(self): print(f"{self.titulo} - {self.autor} ({self.estado})")

libros = [
    Libro("Cien Años de Soledad", "Gabo"),
    Libro("1984", "Orwell", "prestado"),
    Libro("El Principito", "Exupéry")
]

for l in libros: l.mostrar()

op = input("\n1. Prestar (libro 1)\n2. Devolver (libro 2)\nOpción: ")
if op=="1": libros[0].prestar()
elif op=="2": libros[1].devolver()

for l in libros: l.mostrar()
