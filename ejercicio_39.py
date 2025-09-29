class Empleado: 
    def __init__(self,n,r): self.nombre,self.rol=n,r
class Tarea: 
    def __init__(self,n,d): self.nombre,self.duracion=n,d; self.completada=False; self.dependencias=[]
    def dep(self,t): self.dependencias.append(t)
    def completar(self):
        if all(t.completada for t in self.dependencias): self.completada=True
class Equipo: 
    def __init__(self,n): self.nombre=n; self.miembros=[]
    def agregar(self,e): self.miembros.append(e)
class Proyecto:
    def __init__(self,n): self.nombre=n; self.tareas=[]; self.equipo=None
    def asignar_equipo(self,e): self.equipo=e
    def agregar_tarea(self,t): self.tareas.append(t)
    def cronograma(self):
        for t in self.tareas: print(f"{t.nombre} ({t.duracion}d) - {'Completada' if t.completada else 'Pendiente'} deps: {[d.nombre for d in t.dependencias]}")

# Ejemplo
e1,e2=Empleado("Ana","Dev"),Empleado("Luis","Tester")
eq=Equipo("A"); eq.agregar(e1); eq.agregar(e2)
p=Proyecto("App"); p.asignar_equipo(eq)
t1,t2,t3=Tarea("UI",5),Tarea("Backend",10),Tarea("Pruebas",3)
t3.dep(t1); t3.dep(t2)
p.agregar_tarea(t1); p.agregar_tarea(t2); p.agregar_tarea(t3)
t1.completar(); t2.completar(); t3.completar()
p.cronograma()
