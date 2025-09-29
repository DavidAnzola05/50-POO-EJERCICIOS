class Usuario: 
    def __init__(self,n,c): self.nombre,self.correo=n,c
class Producto: 
    def __init__(self,n,p): self.nombre,self.precio=n,p
class Carrito: 
    def __init__(self): self.items=[]
    def agregar(self,p,c=1): self.items.append((p,c))
    def total(self): return sum(p.precio*c for p,c in self.items)
class Orden:
    def __init__(self,u,car): self.usuario,u,self.items= u,car.items; self.pagada=False
    def pagar(self,metodo="tarjeta"): self.pagada=True; print(f"{self.usuario.nombre} pagó ${self.total()} con {metodo}")
    def total(self): return sum(p.precio*c for p,c in self.items)

u=Usuario("Ana","ana@mail.com")
p1,p2=Producto("Camiseta",20),Producto("Pantalón",35)
c=Carrito(); c.agregar(p1,2); c.agregar(p2)
o=Orden(u,c); o.pagar("PayPal")
