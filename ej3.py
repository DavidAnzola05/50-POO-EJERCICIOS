class Cuenta:
    def __init__(self, saldo=0): self.saldo=saldo
    def depositar(self,m): self.saldo+=m if m>0 else 0; print(f"Saldo: {self.saldo}")
    def retirar(self,m): print(f"Saldo: {self.saldo-m}" if 0<m<=self.saldo else "Fondos insuficientes"); 
    def consultar(self): print(f"Saldo: {self.saldo}")

c=Cuenta(1000)
while True:
    o=input("\n1.Depositar  2.Retirar  3.Saldo  4.Salir: ")
    if o=='1': c.depositar(float(input("Monto: ")))
    elif o=='2': c.retirar(float(input("Monto: ")))
    elif o=='3': c.consultar()
    elif o=='4': break
    else: print("Opción inválida")

        print("Opcion invalida. Intente de nuevo.")
