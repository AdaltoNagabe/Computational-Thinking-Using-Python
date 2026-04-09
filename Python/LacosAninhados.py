a = input("Digite o primeiro valor: ")
b = input("Digite o segundo valor: ")
c = input("Digite o terceiro valor: ")

menor = a
if b < menor:
    menor = b
    
    if  c < menor:
        menor = c
print(menor)
                
            