import sys
import os

sys.path.append(os.path.abspath("src"))

from biblioteca.biblioteca import Biblioteca

CAMINHO = "data/test_biblioteca.json"


def setup_function():
    if os.path.exists(CAMINHO):
        os.remove(CAMINHO)


def test_adicionar_e_listar():
    b = Biblioteca(CAMINHO)
    b.adicionar("Livro A", "Autor A")
    b.adicionar("Livro B", "Autor B")

    livros = b.listar()
    assert len(livros) == 2


def test_buscar():
    b = Biblioteca(CAMINHO)
    b.adicionar("Python Básico", "Autor A")
    b.adicionar("Python Avançado", "Autor B")

    resultado = b.buscar("Python")
    assert len(resultado) == 2


def test_atualizar():
    b = Biblioteca(CAMINHO)
    b.adicionar("Antigo", "Autor")
    livro = b.listar()[0]

    b.atualizar(livro.id, "Novo", "Autor X")
    atualizado = b.listar()[0]

    assert atualizado.titulo == "Novo"


def test_remover():
    b = Biblioteca(CAMINHO)
    b.adicionar("Livro", "Autor")
    livro = b.listar()[0]

    b.remover(livro.id)
    assert len(b.listar()) == 0


def test_persistencia():
    b = Biblioteca(CAMINHO)
    b.adicionar("Persistente", "Autor")
    b.salvar()

    b2 = Biblioteca(CAMINHO)
    assert len(b2.listar()) == 1
