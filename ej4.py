class ListaTareas:
    def __init__(self): self.tareas = []
    def agregar(self, t): self.tareas.append(t); print(f"'{t}' agregada.")
    def eliminar(self, t): print(f"'{t}' eliminada.") if t in self.tareas and not self.tareas.remove(t) else print(f"'{t}' no encontrada.")
    def completar(self, t): print(f"'{t}' completada." if t in self.tareas else f"'{t}' no encontrada.")
    def mostrar(self): print("\n".join(f"{i+1}. {t}" for i,t in enumerate(self.tareas)) or "Sin tareas.")

lista = ListaTareas()
while True:
    opcion = input("\n1.Agregar 2.Eliminar 3.Completar 4.Mostrar 5.Salir: ")
    if   opcion == '1': lista.agregar(input("Tarea: "))
    elif opcion == '2': lista.eliminar(input("Tarea: "))
    elif opcion == '3': lista.completar(input("Tarea: "))
    elif opcion == '4': lista.mostrar()
    elif opcion == '5': break
    else: print("Opción inválida.")
