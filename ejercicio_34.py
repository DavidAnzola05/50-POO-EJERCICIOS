class Profesor: 
    def __init__(self,n,i): self.nombre, self.instrumento = n,i

class Estudiante: 
    def __init__(self,n,i): self.nombre,self.instrumento,self.progreso=n,i,0
    def avanzar(self,p): self.progreso=min(100,self.progreso+p)

class Clase: 
    def __init__(self,n,prof): self.nombre,self.profesor,self.estudiantes=n,prof,[]
    def agregar(self,e): self.estudiantes.append(e)

# Ejemplo
p=Profesor("Laura","Piano")
e=Estudiante("Ana","Piano")
c=Clase("Piano Básico",p)
c.agregar(e)
e.avanzar(20)
print(e.nombre,e.progreso)
