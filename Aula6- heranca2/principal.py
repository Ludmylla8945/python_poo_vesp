from pessoa import Pessoa, Aluno, Professor

pessoa1 = Pessoa("Ludmylla", 18)
aluno1 = Aluno("João", 14, 998)

pessoa1.info()

aluno1.info()
aluno1.estudar()

professor1 = Professor("Bruno", 33, "Programacao")
professor1.info()
professor1.ensinar()