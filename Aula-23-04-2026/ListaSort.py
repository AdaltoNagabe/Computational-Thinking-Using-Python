vetor = [1,2,3,4,5,6,7,8,9,10]

vetor.sort() #Ordena a lista em ordem crescente, ou seja, a lista agora é [1,2,3,4,5,6,7,8,9,10]
print(vetor)

vetor.sort(reverse=True) #Ordena a lista em ordem decrescente, ou seja, a lista agora é [10,9,8,7,6,5,4,3,2,1]
print(vetor)

print("------------------------------------")

#Exemplo para pegar as duas maiores notas de um aluno e calcular a média entre elas. Para isso, podemos usar o método sort para ordenar as notas em ordem decrescente, e depois pegar as duas primeiras notas da lista para calcular a média. O código abaixo mostra como fazer isso:
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

VetorNotas = [nota1,nota2,nota3]
print ("As notas sao: " + str(VetorNotas))

VetorNotas.sort(reverse=True)
media = (VetorNotas[0] + VetorNotas[1]) /2
print ("A media das duas maiores e: " + str(media))