from conta import Conta

minhaConta = Conta(321, "Jbuticaba Freitas", 20000)

minhaConta.relatorio()

minhaConta.setLimite(8000)
minhaConta.relatorio() 


print(f"O seu limite atual é {minhaConta.getLimite()}")

minhaConta.depositar(300)
minhaConta.relatorio()

minhaConta.sacar(24)
minhaConta.relatorio()