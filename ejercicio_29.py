from datetime import datetime
class Recurso: 
    def __init__(s,n): s.n, s.disp = n, True
class Usuario: 
    def __init__(s,n): s.n, s.res = n,[]
class Reserva: 
    def __init__(s,r,u): s.r,s.u,s.f=r,u,datetime.now(); r.disp=False; u.res.append(s)

r,u=Recurso("Sala A"),Usuario("Ana")
res=Reserva(r,u)
print(f"{u.n} reservó {r.n} el {res.f:%Y-%m-%d %H:%M}")
