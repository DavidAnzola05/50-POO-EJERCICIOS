class Paciente: 
    def __init__(self,n): self.nombre=n; self.historial=[]
    def agregar_tratamiento(self,t): self.historial.append(t)

class Doctor: 
    def __init__(self,n,esp): self.nombre=n; self.especialidad=esp

class Departamento: 
    def __init__(self,n): self.nombre=n; self.doctores=[]; self.pacientes=[]
    def agregar_doctor(self,d): self.doctores.append(d)
    def agregar_paciente(self,p): self.pacientes.append(p)

class Tratamiento: 
    def __init__(self,n,desc): self.nombre=n; self.descripcion=desc

# Ejemplo
p=Paciente("Ana"); d=Doctor("Luis","Cardiología")
dep=Departamento("Cardio"); dep.agregar_doctor(d); dep.agregar_paciente(p)
t=Tratamiento("Chequeo","Revisión anual"); p.agregar_tratamiento(t)
print(p.nombre, [(tr.nombre,tr.descripcion) for tr in p.historial], d.nombre, dep.nombre)
