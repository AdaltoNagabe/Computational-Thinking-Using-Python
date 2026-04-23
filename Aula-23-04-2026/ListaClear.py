# Outro metodo perigoso, pois ele modifica a lista original, ou seja, a lista original é modificada para conter os elementos da outra lista. Por isso, é importante ter cuidado ao usar o método clear, pois ele pode causar problemas se a lista original for usada em outras partes do código. O código abaixo mostra um exemplo de como usar o método clear para limpar uma lista:
# O método clear é usado para limpar uma lista, ou seja, para remover todos os elementos da lista. O método clear é diferente do operador del, pois o operador del remove a lista inteira, enquanto o método clear remove apenas os elementos da lista, deixando a lista vazia. O código abaixo mostra um exemplo de como usar o método clear para limpar uma lista:
# Nao tem como recuperar os elementos de uma lista depois de usar o método clear, pois o método clear remove todos os elementos da lista, deixando a lista vazia. Por isso, é importante ter cuidado ao usar o método clear, pois ele pode causar problemas se a lista original for usada em outras partes do código. O código abaixo mostra um exemplo de como usar o método clear para limpar uma lista:

vetor = [1,2,3,4,5,6,7,8,9,10]

vetor.clear() #Limpa a lista, ou seja, a lista agora é []
print(vetor)

# O del diferente do clear exclui a lista inteira enquanto o clear apenas limpa a lista
del vetor #Remove a lista inteira, ou seja, a lista agora é removida da memória, e não é possível acessar a lista depois disso. Por isso, é importante ter cuidado ao usar o operador del, pois ele pode causar problemas se a lista original for usada em outras partes do código. O código abaixo mostra um exemplo de como usar o operador del para remover uma lista:
print(vetor) #Isso vai causar um erro, pois a lista vetor foi removida da memória, e não é possível acessar a lista depois disso. Por isso, é importante ter cuidado ao usar o operador del, pois ele pode causar problemas se a lista original for usada em outras partes do código. O código abaixo mostra um exemplo de como usar o operador del para remover uma lista:

