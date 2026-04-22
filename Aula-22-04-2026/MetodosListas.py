vetorGenerico = [2,4,6,4]
vetorGenerico.append(5) #Insere um novo valor no vetor

print(vetorGenerico)

vetorGenerico.remove(4) #Remove um elemento do vetor, o primeiro que ele encontrar
print(vetorGenerico)

vetorGenerico.pop() #mostra qual foi o elemento excluido
elementoRemovido = vetorGenerico.pop()
print(elementoRemovido)

print("---------------------------")


vetorNotas = [] # Lista vazia

vetorNotas.append(10)  # Preenche a lista a partir do indice 0
vetorNotas.append(5.5)
vetorNotas.append(7.5)
vetorNotas.append(9)

print(vetorNotas)

vetorNotas.count(10)  #Conta elementos semelhante ao cont.se do excel
