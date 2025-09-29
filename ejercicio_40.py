class Cuenta: 
    def __init__(self,n,s=0): self.nombre,n; self.saldo=s; self.trans=[]
    def depositar(self,m): self.saldo+=m; self.trans.append(f"+{m}")
    def retirar(self,m): 
        if m<=self.saldo: self.saldo-=m; self.trans.append(f"-{m}")
class Tarjeta: 
    def __init__(self,c,cod,cuenta): self.num=c; self.cod=cod; self.cuenta=cuenta
class Prestamo: 
    def __init__(self,m,interes): self.monto=m; self.interes=interes; self.pagado=False
    def pagar(self): self.pagado=True
class Transaccion: 
    def __init__(self,tipo,monto): self.tipo=tipo; self.monto=monto

# Ejemplo
c=Cuenta("Ana",1000)
c.depositar(500); c.retirar(200)
t=Tarjeta("1234","999",c)
p=Prestamo(1000,0.05); p.pagar()
print(c.saldo, c.trans, p.pagado)
