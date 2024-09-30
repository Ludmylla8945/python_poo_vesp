# Definindo a classe Livro
class Livro:
    # Construtor da classe
    def __init__(self, titulo, autor, anoPublicacao):
        self.titulo = titulo
        self.autor = autor
        self.anoPublicacao = anoPublicacao

    # Método para exibir as informações do livro
    def exibirInformacoes(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Ano de Publicação: {self.anoPublicacao}")

    # Método para verificar se o livro é um clássico (mais de 50 anos)
    def verificarIdadeLivro(self):
        anoAtual = 2024  # Você pode mudar este valor para um cálculo dinâmico, se preferir
        idadeLivro = anoAtual - self.anoPublicacao
        
        if idadeLivro > 50:
            print("Este livro é um clássico.")
        else:
            print("Ainda não é considerado um clássico.")


