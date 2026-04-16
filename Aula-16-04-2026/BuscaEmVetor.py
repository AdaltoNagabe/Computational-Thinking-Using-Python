vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f'o comprimento do vetor é {len(vetor)}')

varBusca = int(input('Digite um numero para buscar no vetor: '))

for index in range(0,len(vetor)): #len(vetor) retorna o comprimento do vetor, ou seja, a quantidade de elementos que ele possui
    if varBusca == vetor[index]:
        print(f'Número encontrado na posição {index} do vetor')
        print(f'O tamanho do vetor é {len(vetor)}')
        break
    print(index)