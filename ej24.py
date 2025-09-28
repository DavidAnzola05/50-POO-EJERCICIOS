class Cuenta:
    def __init__(self, titular, saldo=0): self.titular, self.saldo = titular, saldo
class Ahorros(Cuenta):
    def __init__(self, titular, saldo=0, interes=0.02): super().__init__(titular, saldo); self.i=interes
    def interes(self): self.saldo+=self.saldo*self.i; return f"Saldo: ${self.saldo:.2f}"
class Corriente(Cuenta):
    def __init__(self, titular, saldo=0, limite=500): super().__init__(titular, saldo); self.l=limite
    def retirar(self,m): 
        if self.saldo-m<-self.l: return "Límite excedido"
        self.saldo-=m; return f"Saldo: ${self.saldo:.2f}"

# Uso
print(Ahorros("Ana",1000).interes())
c=Corriente("Luis",200); print(c.retirar(300)); print(c.retirar(500))
