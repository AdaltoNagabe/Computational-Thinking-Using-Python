#mapeando numeros pares e impares de um vetor de um a cinco

vetor = [1,2,3,4,5]

vetorParesImpares = (("Par" if elemento % 2 == 0 else "Impar") for elemento in vetor)
print ([elemento for elemento in vetor])


print (vetorParesImpares)



#-------------------------------------


numero = []

for num in range(1,20,1):
    numero.append(num)

print(numero)

numero = [numero for numero in range(1,20,1)] # Substitui o for acima



