from livro import Livro

# Criando o primeiro objeto Livro
livro1 = Livro("Dom Casmurro", "Machado de Assis", 1899)

# Criando o segundo objeto Livro
livro2 = Livro("1984", "George Orwell", 1949)

# Chamando os métodos para o primeiro livro
print("Informações do primeiro livro:")
livro1.exibirInformacoes()
livro1.verificarIdadeLivro()

print("\nInformações do segundo livro:")
# Chamando os métodos para o segundo livro
livro2.exibirInformacoes()
livro2.verificarIdadeLivro()