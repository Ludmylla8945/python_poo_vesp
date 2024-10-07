
from academia import Aluno

if __name__ == "__main__":
    # Criando os objetos da classe Aluno
    aluno1 = Aluno("João", 25, 70, 1.75)
    aluno2 = Aluno("Maria", 30, 60, 1.65)
    
    # Exibindo dados e calculando IMC para aluno1
    print(aluno1.exibirDados())
    print(aluno1.calcularIMC())
    
    # Exibindo dados e calculando IMC para aluno2
    print(aluno2.exibirDados())
    print(aluno2.calcularIMC())