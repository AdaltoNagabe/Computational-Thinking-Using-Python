v = [1,2,3,4,2,5,6,7,2]
v.append(4) #Adiciona o valor 4 ao final da lista, ou seja, a lista agora é [1,2,3,4,2,5,6,7,2,4]
print(v)

v.count(2) #Conta quantas vezes o valor 2 aparece na lista, nesse caso, o resultado é 1

#count é um método de lista que conta quantas vezes um determinado valor aparece na lista. Ele retorna o número de ocorrências do valor especificado. Por exemplo, se tivermos a lista [1, 2, 3, 2, 4] e chamarmos list.count(2), o resultado será 2, pois o valor 2 aparece duas vezes na lista.

#neste caso temos um vetor no elemento 6 do vetor, ou seja, a lista [1,2,3], e queremos contar quantas vezes o valor 2 aparece nessa lista, nesse caso, o resultado é 1, pois o valor 2 aparece uma vez na lista [1,2,3].
vetor = [1,2,3,4,'Fulano',True,[1,2,3],[3,2,1]]
vetor[6].count(2) #Conta quantas vezes o valor 2 aparece na lista que está no índice 6 do vetor, ou seja, a lista [1,2,3], nesse caso, o resultado é 1
