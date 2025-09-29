class Usuario: 
    def __init__(self,n): self.nombre=n; self.playlists=[]; self.sus=None
class Contenido: 
    def __init__(self,t,tit): self.tipo,self.titulo=t,tit; self.visto=0
class Playlist: 
    def __init__(self,n): self.nombre=n; self.items=[]
    def agregar(self,c): self.items.append(c)
class Suscripcion: 
    def __init__(self,tipo): self.tipo=tipo; self.activa=True

# Ejemplo
u=Usuario("Ana")
c1,c2=Contenido("P","Matrix"),Contenido("S","Breaking Bad")
pl=Playlist("Favoritos"); [pl.agregar(c) for c in [c1,c2]]; u.playlists.append(pl)
u.sus=Suscripcion("Premium")
c1.visto+=1; c2.visto+=2
print(u.nombre, [p.nombre for p in u.playlists], c1.visto, u.sus.activa)
