v = [1,2,3]
v[2] = 5 #Altera o valor do índice 2 para 5
print(v)

vetorTeste = v #Atribui o valor de v para vetorTeste, ou seja, ambos apontam para a mesma lista
print(vetorTeste)


vetorTeste= v.copy() #Cria uma cópia da lista v e atribui a vetorTeste, ou seja, ambos apontam para listas diferentes   
v[2] = 3 #Altera o valor do índice 2 para 3, mas isso não afeta vetorTeste, pois ele é uma cópia de v
print(v)
print(vetorTeste)

#Podemos criar um vetor de teste para preservar o valor original de v, mesmo que v seja alterada posteriormente
