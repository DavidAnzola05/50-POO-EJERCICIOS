class Usuario:
    def __init__(self,n): self.n,self.s,self.p=n,[],[]
    def seguir(self,o): 
        if o not in self.s:self.s.append(o)
    def publicar(self,t):
        pub={"autor":self.n,"texto":t,"likes":0,"comentarios":[]}
        self.p.append(pub);return pub

# DEMO
u1,u2=Usuario("Ana"),Usuario("Luis")
u1.seguir(u2)
p=u2.publicar("Hola a todos!")
p["likes"]+=1; p["comentarios"].append((u1.n,"Bienvenido!"))
print(f"{p['autor']}: {p['texto']} ❤️{p['likes']}")
for c in p["comentarios"]: print(f"{c[0]}: {c[1]}")
mbre, "comentó:", c.texto)
