class Materia:
    def __init__(self, nombre, creditos):
        self.nombre = nombre
        self.creditos = creditos

class Calificacion:
    def __init__(self, materia, nota):
        self.materia = materia
        self.nota = nota

class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.calificaciones = []

    def agregar_calificacion(self, materia, nota):
        self.calificaciones.append(Calificacion(materia, nota))

    def promedio_ponderado(self):
        if not self.calificaciones:
            return 0
        suma_ponderada = sum(c.nota * c.materia.creditos for c in self.calificaciones)
        suma_creditos = sum(c.materia.creditos for c in self.calificaciones)
        return round(suma_ponderada / suma_creditos, 2)


if __name__ == "__main__":
    m1 = Materia("Matemáticas", 4)
    m2 = Materia("Historia", 2)
    m3 = Materia("Programación", 3)
    e = Estudiante("Mateo")
    e.agregar_calificacion(m1, 4.5)
    e.agregar_calificacion(m2, 3.8)
    e.agregar_calificacion(m3, 5.0)
    print(e.nombre, "Promedio:", e.promedio_ponderado())
