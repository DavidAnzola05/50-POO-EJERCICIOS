class Elemento:
    def __init__(self, nombre): self.nombre = nombre
    def mostrar(self): print(self.nombre)

class Archivo(Elemento):
    def __init__(self, nombre, tamano):
        super().__init__(nombre); self.tamano = tamano
    def mostrar(self): print(f"Archivo: {self.nombre}, {self.tamano} bytes")

class Carpeta(Elemento):
    def __init__(self, nombre):
        super().__init__(nombre); self.contenido = []
    def agregar(self, elem): self.contenido.append(elem)
    def mostrar(self):
        print(f"Carpeta: {self.nombre}")
        for e in self.contenido: e.mostrar()

# Construcción del sistema
raiz = Carpeta("raiz")
docs, imgs = Carpeta("Documentos"), Carpeta("Imágenes")
raiz.agregar(docs); raiz.agregar(imgs)
docs.agregar(Archivo("archivo1.txt", 1200))
imgs.agregar(Archivo("foto.jpg", 250000))
raiz.agregar(Archivo("presentacion.pptx", 45000))

# Mostrar estructura
raiz.mostrar()
