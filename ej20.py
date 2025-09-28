class Instrumento:
    def __init__(self, nombre, tipo, detalle):
        self.nombre, self.tipo, self.detalle = nombre, tipo, detalle
    def tocar(self):
        print(f"Tocando {self.nombre}, instrumento de tipo {self.tipo}.")
        return self.detalle

guitarra = Instrumento("Guitarra Eléctrica", "Cuerda", "Tiene 6 cuerdas.")
piano = Instrumento("Piano de Cola", "Teclado", "Tiene 88 teclas.")
bateria = Instrumento("Batería Acústica", "Percusión", "Es de tamaño grande.")

for i in (guitarra, piano, bateria):
    print(i.tocar())
