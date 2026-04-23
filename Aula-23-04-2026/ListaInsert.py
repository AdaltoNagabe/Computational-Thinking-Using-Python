vetor = [1,2,3,4,'Fulano',True,[1,2,3],[3,2,1]]
elementoExtraido = vetor.pop() #Remove o último elemento da lista, ou seja, a lista [3,2,1] é removida da lista, e a lista agora é [1,2,3,4,'Fulano',True,[1,2,3]]
print("Foi extraído o elemento:", elementoExtraido)
print(vetor) 

#para recuperar o elemento extraido pelo pop, podemos usar o método insert para inserir o elemento extraído de volta na lista. O método insert recebe dois parâmetros: o índice onde o elemento deve ser inserido e o elemento a ser inserido. No caso, queremos inserir o elemento extraído no índice -1 da lista, ou seja, na penúltima posição da lista. Então, podemos usar o código abaixo para recuperar o elemento extraído:
vetor.insert(7,elementoExtraido) #Insere o elemento extraído no índice -1 da lista, ou seja, o elemento [3,2,1] é inserido na penúltima posição da lista, e a lista agora é [1,2,3,4,'Fulano',True,[1,2,3],[3,2,1]]
print(vetor)

vetor.insert(-1,10) #Insere o valor 10 na última posição da lista, e a lista agora é [1,2,3,4,'Fulano',True,[1,2,3],[3,2,1],10]
print(vetor)
