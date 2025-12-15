class Livro:
    def __init__(self, id, titulo, autor):
        self.id = id
        self.titulo = titulo
        self.autor = autor

    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "autor": self.autor
        }

    @staticmethod
    def from_dict(dados):
        return Livro(
            dados["id"],
            dados["titulo"],
            dados["autor"]
        )
