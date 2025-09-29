from datetime import datetime
class Paciente: 
    def __init__(s,n): s.n,s.hist=n,[]
class Doctor: 
    def __init__(s,n): s.n=n
class Cita: 
    def __init__(s,p,d,f): s.p,s.d,s.f=p,d,f; p.hist.append(s)

p,d=Paciente("Ana"),Doctor("Dr. Luis")
c=Cita(p,d,datetime(2025,9,30,10,0))
print(f"{c.p.n} tiene cita con {c.d.n} el {c.f:%Y-%m-%d %H:%M}")
