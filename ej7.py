class ContadorTexto:
    def __init__(self, texto): self.texto = texto
    def contar_palabras(self): return len(self.texto.split())
    def contar_caracteres(self): return len(self.texto)
    def contar_lineas(self): return len(self.texto.splitlines())

t = ContadorTexto(input("Ingrese un texto: "))
print("El texto tiene:")
print(f"{t.contar_palabras()} palabras")
print(f"{t.contar_caracteres()} caracteres")
print(f"{t.contar_lineas()} líneas")
