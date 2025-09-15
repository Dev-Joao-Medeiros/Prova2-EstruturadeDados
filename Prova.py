class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.acervo = {}       
        self.emprestados = {}

    def adicionar_livro(self, livro, quantidade):
        self.acervo[livro] = self.acervo.get(livro, 0) + quantidade
        print(f"{quantidade} livros de '{livro}' adicionados na biblioteca.")

    def emprestar_livro(self, livro):
        if livro in self.acervo and self.acervo[livro] > 0:
            self.acervo[livro] -= 1
            self.emprestados[livro] = self.emprestados.get(livro, 0) + 1
            print(f"Livro '{livro}' emprestado com sucesso.")
        else:
            print("Livro não disponível para empréstimo.")

    def devolver_livro(self, livro):
        if livro in self.emprestados and self.emprestados[livro] > 0:
            self.emprestados[livro] -= 1
            self.acervo[livro] = self.acervo.get(livro, 0) + 1
            print(f"Livro '{livro}' devolvido com sucesso.")
        else:
            print("Este livro não está marcado como emprestado.")

    def exibir_situacao(self):
        print(f"\n{self.nome}")
        print("Livros disponíveis:")
        if self.acervo:
            for livro, qtd in self.acervo.items():
                print(f"  {livro}: {qtd}")
        else:
            print("Nenhum livro disponível.")

        print("\nLivros emprestados:")
        if self.emprestados:
            for livro, qtd in self.emprestados.items():
                print(f"  {livro}: {qtd}")
        else:
            print("Nenhum livro emprestado.")

        print(f"\nTotal disponíveis: {sum(self.acervo.values())}")
        print(f"Total emprestados: {sum(self.emprestados.values())}")


def main():
    biblioteca = Biblioteca("Biblioteca Comunitaria")

    while True:
        print("\n--- MENU ---")
        print("1 - Adicionar livros")
        print("2 - Emprestar livro")
        print("3 - Devolver livro")
        print("4 - Exibir situacao dos livros")
        print("5 - Sair")
        opcao = input("Escolha uma opcao: ")

        if opcao == "1":
            livro = input("Digite o nome do livro: ").lower()
            qtd = int(input("Digite a quantidade: "))
            biblioteca.adicionar_livro(livro, qtd)

        elif opcao == "2":
            livro = input("Digite o nome do livro que deseja emprestar: ").lower()
            biblioteca.emprestar_livro(livro)

        elif opcao == "3":
            livro = input("Digite o nome do livro que deseja devolver: ").lower()
            biblioteca.devolver_livro(livro)

        elif opcao == "4":
            biblioteca.exibir_situacao()

        elif opcao == "5":
            print("Encerrando o sistema... Ate mais tarde!")
            break
        else:
            print("Opção inválida! Digite um valor valido.")

if __name__ == "__main__":
    main()