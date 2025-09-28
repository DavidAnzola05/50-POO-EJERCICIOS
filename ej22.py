class Usuario:
    def __init__(self, nombre, contraseña, cargo):
        self.nombre, self.contraseña, self.cargo = nombre, contraseña, cargo
    def permisos(self):
        return f"El usuario {self.nombre} tiene permisos de {self.cargo.lower()}."
usuarios = [
    Usuario("adminUser", "adminPass", "Administrador"),
]
for u in usuarios:
    print(u.permisos())
    print(f"Usuario: {u.nombre}, Cargo: {u.cargo}")
