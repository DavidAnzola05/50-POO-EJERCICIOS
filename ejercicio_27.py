class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.seguidos = []
        self.publicaciones = []

    def seguir(self, otro):
        if otro not in self.seguidos:
            self.seguidos.append(otro)

    def publicar(self, contenido):
        p = Publicacion(self, contenido)
        self.publicaciones.append(p)
        return p


class Publicacion:
    def __init__(self, autor, contenido):
        self.autor = autor
        self.contenido = contenido
        self.likes = 0
        self.comentarios = []

    def dar_like(self):
        self.likes += 1

    def comentar(self, usuario, texto):
        c = Comentario(usuario, texto)
        self.comentarios.append(c)
        return c


class Comentario:
    def __init__(self, autor, texto):
        self.autor = autor
        self.texto = texto


if __name__ == "__main__":
    u1 = Usuario("Ana")
    u2 = Usuario("Luis")
    u1.seguir(u2)
    pub = u2.publicar("Hola a todos!")
    pub.dar_like()
    pub.comentar(u1, "Bienvenido!")
    print(pub.contenido, "Likes:", pub.likes)
    for c in pub.comentarios:
        print(c.autor.nombre, "comentó:", c.texto)
