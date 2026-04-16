vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for index in range(len(vetor)):
    print(f'Vetor na posição {index} é igual a {vetor[index]}')
 
print('-------------------------------')
    
for index in range(0,len(vetor),2): #Comeca na posicao 0 do vetor pulando de 2 em 2
    print(f'Vetor na posição {index} é igual a {vetor[index]}')
    
print('-------------------------------')    
for x in range(len(vetor)): #A palavra index é uma convenção, mas pode ser qualquer nome, como x, y, z, etc
    print(f'Vetor na posição {x} é igual a {vetor[x]}')


    
     
    