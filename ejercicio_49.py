class Neurona: 
    def __init__(self,pesos,bias): self.pesos=pesos; self.bias=bias
    def activar(self,x): return sum(w*i for w,i in zip(self.pesos,x))+self.bias

class Red: 
    def __init__(self,neuronas): self.neuronas=neuronas
    def forward(self,entrada): return [n.activar(entrada) for n in self.neuronas]

class Entrenamiento: 
    def __init__(self,red): self.red=red
    def entrenar(self,entradas,targets,lr=0.1):
        for x,t in zip(entradas,targets):
            salida=self.red.forward(x)
            for n,o in zip(self.red.neuronas,salida):
                for i in range(len(n.pesos)):
                    n.pesos[i]+=lr*(t-o)*x[i]
                n.bias+=lr*(t-o)

class Prediccion: 
    def __init__(self,red): self.red=red
    def predecir(self,x): return self.red.forward(x)

# Ejemplo
n1,n2=Neurona([0.5,0.5],0.1),Neurona([0.3,0.7],-0.1)
r=Red([n1,n2])
ent=Entrenamiento(r)
entradas=[[1,0],[0,1]]; targets=[[1,0],[0,1]]
ent.entrenar(entradas,targets)
pred=Prediccion(r)
print(pred.predecir([1,0]))
