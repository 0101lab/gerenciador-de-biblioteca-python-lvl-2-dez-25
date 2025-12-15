from biblioteca.biblioteca import Biblioteca

def main():
    biblioteca = Biblioteca("data/biblioteca.json")

    while True:
        print("\n1 - Cadastrar")
        print("2 - Listar")
        print("3 - Buscar")
        print("4 - Atualizar")
        print("5 - Remover")
        print("0 - Sair")

        opcao = input("> ")

        try:
            if opcao == "1":
                biblioteca.adicionar(
                    input("Título: "),
                    input("Autor: ")
                )

            elif opcao == "2":
                for livro in biblioteca.listar():
                    print(livro.id, livro.titulo, "-", livro.autor)

            elif opcao == "3":
                for livro in biblioteca.buscar(input("Buscar: ")):
                    print(livro.id, livro.titulo)

            elif opcao == "4":
                biblioteca.atualizar(
                    int(input("ID: ")),
                    input("Novo título: "),
                    input("Novo autor: ")
                )

            elif opcao == "5":
                biblioteca.remover(int(input("ID: ")))

            elif opcao == "0":
                biblioteca.salvar()
                break

        except Exception as e:
            print("Erro:", e)


if __name__ == "__main__":
    main()
