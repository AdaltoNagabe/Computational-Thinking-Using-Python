#Funcao anonima
varFuncao = lambda var: 1*var**2 + 2*var + 1
print(varFuncao(7))

#Funcao padrao
def funcaoSegundoGrau(numero):
    #Funcao (subalgoritmo) que aplica uma funcao do 2º grau a um numero 
    numeroSegundoGrau = 1*numero**2 + 2*numero + 1
    print(numeroSegundoGrau)
      
#chamando a funcao
funcaoSegundoGrau(7)


def media (a,b):
    soma = a + b
    media = soma/2
    print(media)
    
    media(6,7)