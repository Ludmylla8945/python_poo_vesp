#Importando o arquivo 'pessoa' e dentro desse arquivo estamos a classe 'Pessoa'
from pessoa import Pessoa

#Criando Objetos 
p1 = Pessoa("Joana","Correr","Rua do Santo Antonio")
p1.exibirHobby()
p1.mudarHobby("Natação")

#SOLICITANDO DADOS DO USUÁRIO
nomePessoa = input("Informe o nome da pessoa:")
hobbyPessoa = input("Informe o hobby da pessoa:")
endPessoa = input("Qual o endereço?")

p2 = Pessoa(nomePessoa, hobbyPessoa, endPessoa)
p2.exibirHobby()