import json
import os
from .livro import Livro

class Biblioteca:
    def __init__(self, caminho_arquivo):
        self.caminho_arquivo = caminho_arquivo
        self.livros = []
        self._carregar()

    def adicionar(self, titulo, autor):
        pass

    def listar(self):
        pass

    def buscar(self, termo):
        pass

    def atualizar(self, id_livro, titulo, autor):
        pass

    def remover(self, id_livro):
        pass

    def _carregar(self):
        pass

    def salvar(self):
        pass
