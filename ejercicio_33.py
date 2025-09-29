class Cliente: 
    def __init__(s,n): s.n,s.peds=n,[]
class Pedido: 
    def __init__(s,c): s.c,s.est,s.dets=c,"Pendiente",[]; c.peds.append(s)
class DetallePedido: 
    def __init__(s,p,it,c): s.it,s.c=it,c; p.dets.append(s)

c=Cliente("Ana")
p=Pedido(c)
DetallePedido(p,"Laptop",1)
print(f"Cliente {c.n} hizo un pedido de {p.dets[0].c} {p.dets[0].it}, Estado: {p.est}")
