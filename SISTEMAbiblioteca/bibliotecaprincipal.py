from biblioteca import Biblioteca, Livro, Revista

ano_atual = 2024

a1 = Biblioteca("Dom Casmurro", "Machado de Assis", 1899, 208)
p1 = Livro("Dom Casmurro", "Machado de Assis", 1899, 208)

a1.detalhes()

p1.calcularIdadeItem(ano_atual)
p1.verificarTamanho()

print("="*50)

a2 = Biblioteca("Revista Época", "Diego Escosteguy", 1995, 200)
p2 = Revista("Revista Época", "Diego Escosteguy", 1995, 200)

a2.detalhes()

p2.calcularIdadeItem(ano_atual)
p2.verificarEdicao()
