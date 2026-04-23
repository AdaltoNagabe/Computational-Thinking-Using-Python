# Tuplas e semelhante a lista mas e imutavel

vetor = [1,2,3,4,5,6,7,8,9,10]

tuple = (1,2,3,4,5,6,7,8,9,10) #As tuplas são imutáveis, ou seja, não é possível adicionar ou remover elementos de uma tupla, ou seja, a tupla sempre será (1,2,3,4,5,6,7,8,9,10)
print("A tupla é:", tuple)

# Casting de lista para tupla
tupla1 = tuple(vetor) #Converte a lista vetor em uma tupla, ou seja, a tupla agora é (1,2,3,4,5,6,7,8,9,10)
print("O vetor convertido é:", tupla1)

# Estes sao os unicos metodos aceitos para tuplas, pois as tuplas sao imutaveis, ou seja, nao e possivel adicionar ou remover elementos de uma tupla, ou seja, a tupla sempre sera (1,2,3,4,5,6,7,8,9,10)
tupla1.count(2) #Retorna o número de vezes que o elemento 2 aparece na tupla, ou seja, o número 2 aparece 1 vez na tupla, então o número 1 é retornado
tupla1.index(2) #Retorna o índice do elemento 2 na tupla, ou seja, o número 2 está no índice 1 da tupla, então o número 1 é retornado   
max(tupla1) #Retorna o maior elemento da tupla, ou seja, o número 10 é retornado
min(tupla1) #Retorna o menor elemento da tupla, ou seja, o número 1 é retornado
sum(tupla1) #Retorna a soma de todos os elementos da tupla, ou seja, a soma dos números de 1 a 10 é 55

# Casting de tupla para lista
tupla1 = list(tupla1) #Converte a tupla tupla1 em uma lista, ou seja, a lista agora é [1,2,3,4,5,6,7,8,9,10]
print("A tupla convertida é:", tupla1)