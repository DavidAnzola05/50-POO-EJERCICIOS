class Clase46A:
class Freelancer: 
    def __init__(self,n): self.nombre=n; self.calificaciones=[]
    def calificar(self,punt): self.calificaciones.append(punt)
class Cliente: 
    def __init__(self,n): self.nombre=n
class Proyecto: 
    def __init__(self,t,cliente): self.titulo=t; self.cliente=cliente; self.propuestas=[]
    def agregar_propuesta(self,p): self.propuestas.append(p)
class Propuesta: 
    def __init__(self,freelancer,precio): self.freelancer=freelancer; self.precio=precio

# Ejemplo
f=Freelancer("Ana"); c=Cliente("EmpresaX")
p=Proyecto("Web",c); prop=Propuesta(f,500)
p.agregar_propuesta(prop)
f.calificar(5)
print(f.nombre, f.calificaciones, p.titulo, [(pr.freelancer.nombre,pr.precio) for pr in p.propuestas])
