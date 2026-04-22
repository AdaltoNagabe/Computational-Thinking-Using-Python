VetorNotas = [7,8,9,4,5]
#for index in range(0,len(VetorNotas)):
#  print(VetorNotas[index])

#for index in range(0,3):
#  print (index)

VetorNotas.sort(reverse=True) # Ordena em ordem decrescente
print(VetorNotas)
print("------------------")
VetorNotas.sort() # Ordena em ordem crescente
print(VetorNotas)

VetorNotas[0:3] # Seleciona os valores conforme os indice aplicados [Onde comeca Indice : onde termina len do vetor]