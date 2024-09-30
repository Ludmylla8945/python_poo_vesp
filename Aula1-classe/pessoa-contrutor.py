class Pessoa:
    # Criar o método construtor
    def __init__(self, nome, altura, idade):
        #estamos criando os atributos da classe utilizando o método construtor.
        self.nome = nome
        self.altura = altura
        self.idade = idade

    #criando os métodos
    def exibirDados(self):
        print(f"Ola {self.nome}, sua altura é {self.altura} e sua idade é {self.idade}")

#Criando objeto
p1 = Pessoa("Getulio",1.87,99)
p2 = Pessoa("Tatiana",1.72,75)

p1.exibirDados()
p2.exibirDados()