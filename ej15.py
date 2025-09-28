import time

class Semaforo:
    def __init__(self):
        self.estados = [("rojo", 5), ("amarillo", 2), ("verde", 4)]
        self.i = 0
    def iniciar(self, ciclos=3):
        for _ in range(ciclos*len(self.estados)):
            e, t = self.estados[self.i]
            print(f"El semáforo está en {e.upper()}")
            time.sleep(t)
            self.i = (self.i+1) % len(self.estados)

Semaforo().iniciar()
print("Simulación finalizada.")
