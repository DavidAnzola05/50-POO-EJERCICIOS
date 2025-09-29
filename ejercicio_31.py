class Vehiculo:
    def __init__(s,n): s.n,s.r=n,None
class Ruta:
    def __init__(s,o,d,h): s.o,s.d,s.h=o,d,h
class Pasajero:
    def __init__(s,n): s.n
    def abordar(s,v): print(f"{s.n} aborda {v.n} hacia {v.r.d} a las {v.r.h}")

v=Vehiculo("Bus 1")
v.r=Ruta("Centro","Barrio", "08:00")
p=Pasajero("Ana")
p.abordar(v)
