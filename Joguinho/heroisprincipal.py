from heroisvsviloes import Personagem, Heroi, Vilao

# Criando objetos
heroi = Heroi(nome="Capitão Valor", identidadeSecreta="John Doe")
vilao = Vilao(nome="Senhor Trevas")
personagem_comum = Personagem(nome="Aliado Comum", rank="Intermediário")

# Chamando métodos do Herói
heroi.detalhes()
heroi.executarHabilidade("Raio de Energia")
heroi.verificarVida()
heroi.recarregarEnergia()
heroi.chamarAliado("Lâmina Dourada")

# Chamando métodos do Vilão
vilao.detalhes()
vilao.desferirGolpe("Chama Negra")
vilao.planejarArmadilha("Maldição")
vilao.verificarVida()
vilao.fugir("Teleporte Dimensional")

# Chamando métodos do Personagem Comum
personagem_comum.detalhes()
personagem_comum.receberDano(50)
personagem_comum.verificarVida()


