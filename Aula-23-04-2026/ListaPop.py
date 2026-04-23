vetor = [1,2,3,4,'Fulano',True,[1,2,3],[3,2,1]]
vetor.pop(0) #Remove o elemento no índice 0 da lista, ou seja, o valor 1 é removido da lista, e a lista agora é [2,3,4,'Fulano',True,[1,2,3],[3,2,1]]
print(vetor)

vetor.pop() #Remove o último elemento da lista, ou seja, a lista [3,2,1] é removida da lista, e a lista agora é [2,3,4,'Fulano',True,[1,2,3]]
elementoExtraido = vetor.pop() 
print("Foi extraído o elemento:", elementoExtraido)
print(vetor)
