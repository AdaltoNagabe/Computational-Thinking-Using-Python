vetor = [45,-89,32,-12,33]
listNegativo = []
for indice in range(len(vetor)):
        if vetor[indice] < 0:
                listNegativo.append(vetor[indice])
                vetor[indice] = 0
print(vetor)
print(listNegativo)