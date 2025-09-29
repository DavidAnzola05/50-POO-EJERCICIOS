class Candidato: 
    def __init__(self,n): self.nombre,self.votos=n,0
class Votante: 
    def __init__(self,n): self.nombre,self.voto=n,None
class Eleccion:
    def __init__(self): self.candidatos,self.votantes=[],[]
    def agregar_candidato(self,c): self.candidatos.append(c)
    def agregar_votante(self,v): self.votantes.append(v)
    def votar(self,votante,candidato):
        if votante.voto is None: votante.voto=candidato.nombre;candidato.votos+=1
    def resultados(self): print({c.nombre:c.votos for c in self.candidatos})

# Ejemplo
c1,C2= Candidato("Alice"),Candidato("Bob")
v1,v2= Votante("Juan"),Votante("Maria")
elec=Eleccion(); elec.agregar_candidato(c1); elec.agregar_candidato(C2)
elec.agregar_votante(v1); elec.agregar_votante(v2)
elec.votar(v1,c1); elec.votar(v2,C2); elec.resultados()
