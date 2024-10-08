class Pessoa:  #Classe Mãe
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade 
    def info(self):
        print(f"Nome: {self._nome} Idade: {self._idade}")

#Classe filha 1- aluno
class Aluno(Pessoa):
    def __init__(self, nome, idade, matrícula):
        super().__init__(nome, idade)
        self._matrícula = matrícula

    def estudar(self):
        print(f"{self._nome}, está matrículado com o código: {self._matrícula} e continua estudando normalmente")

#Classe filha 2- Professor
class Professor(Pessoa):
    def __init__(self, nome, idade, disciplina):
        super().__init__(nome, idade)
        self._disciplina = disciplina
    def ensinar(self):
        print(f"{self._nome}, professor da disciplina: {self._disciplina}, está ensinando ")