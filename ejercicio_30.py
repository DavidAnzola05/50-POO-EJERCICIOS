class Personaje:
    def __init__(s,n,hp=100): s.n,s.hp,s.xp=n,hp,0
    def atacar(s,o,d): o.hp-=d; print(f"{s.n} ataca {o.n} y quita {d}, HP {o.n}={o.hp}")
    def curar(s,c): s.hp+=c; print(f"{s.n} se cura {c}, HP={s.hp}")
    def xpup(s,x): s.xp+=x; print(f"{s.n} gana {x} XP, total={s.xp}")

p1,p2=Personaje("Héroe"),Personaje("Orco",80)
p1.atacar(p2,20)
p2.atacar(p1,15)
p1.curar(30)
p1.xpup(50)
