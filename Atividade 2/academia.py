class Aluno:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def exibirDados(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Peso: {self.peso}kg, Altura: {self.altura}m"

    def calcularIMC(self):
        imc = self.peso / (self.altura ** 2)
        return f"O IMC de {self.nome} é {imc:.2f}"

