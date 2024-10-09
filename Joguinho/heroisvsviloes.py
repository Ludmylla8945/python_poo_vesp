class Personagem:
    def __init__(self, nome, vida=100, rank="Novato"):
        self._nome = nome
        self._vida = vida
        self._rank = rank

    def receberDano(self, dano):
        self._vida -= dano
        print(f"{self._nome} recebeu {dano} de dano!")

    def verificarVida(self):
        if self._vida <= 0:
            print(f"{self._nome} está morto.")
        else:
            print(f"{self._nome} ainda está vivo com {self._vida} de vida.")

    def detalhes(self):
        print(f"Nome: {self._nome}, Vida: {self._vida}, Rank: {self._rank}")


class Heroi(Personagem):
    def __init__(self, nome, identidadeSecreta, energia=50, vida=100, rank="Novato"):
        super().__init__(nome, vida, rank)
        self._identidadeSecreta = identidadeSecreta
        self._energia = energia

    def executarHabilidade(self, tipoHabilidade):
        if self._energia >= 10:  # Supondo que cada habilidade consome 10 de energia
            self._energia -= 10
            print(f"{self._nome} executou a habilidade {tipoHabilidade} e consumiu 10 de energia!")
        else:
            print(f"{self._nome} não tem energia suficiente para executar {tipoHabilidade}.")

    def recarregarEnergia(self):
        self._energia += 5
        print(f"{self._nome} recarregou 5 de energia! Energia atual: {self._energia}")

    def chamarAliado(self, nomeAliado):
        print(f"{self._nome} chamou {nomeAliado} para ajudar na luta!")


class Vilao(Personagem):
    def __init__(self, nome, malicia=70, vida=100, rank="Novato"):
        super().__init__(nome, vida, rank)
        self._malicia = malicia

    def desferirGolpe(self, tipoGolpe):
        if self._malicia >= 15:  # Supondo que cada golpe consome 15 de malícia
            self._malicia -= 15
            print(f"{self._nome} desferiu o golpe {tipoGolpe} e consumiu 15 de malícia!")
        else:
            print(f"{self._nome} não tem malícia suficiente para desferir {tipoGolpe}.")

    def planejarArmadilha(self, tipoArmadilha):
        print(f"{self._nome} está planejando a armadilha {tipoArmadilha}.")

    def fugir(self, tipoFulga):
        print(f"{self._nome} conseguiu escapar usando a técnica {tipoFulga}!")
