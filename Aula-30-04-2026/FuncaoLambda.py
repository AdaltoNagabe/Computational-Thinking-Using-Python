#Funcao anonima
varFuncao = lambda var: 1*var**2 + 2*var + 1
print(varFuncao(7))



vetor = [1,2,3,4,5]
vetorMapeado = map(lambda var: var**2, vetor)
print(list(vetorMapeado))


bla = filter(lambda var: var % 2 == 0,vetor)
print(list(bla))