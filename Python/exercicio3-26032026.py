produto = "Pao"
quantidade = 15
preco = 0.50

print(f"Produto: {produto} Quantidade: {quantidade} Preço: {preco}")
print("Produto: {} Quantidade: {} Preço: {}".format(produto, quantidade, preco))
print("Produto: {0} Quantidade: {1} Preço: {2}".format(produto, quantidade, preco))

print("--------------------------------------")

kilometragem = 123.5
volumeCombustivel = 10.5
print(kilometragem/volumeCombustivel)

print("A taxa de consumo do veiculo é de {:.2f} km/l".format(kilometragem/volumeCombustivel))
#Os dois pontos : dentro das chaves {} indicam que queremos formatar o número de uma maneira específica. O .2f indica que queremos formatar o número como um float com 2 casas decimais. Isso significa que o resultado da divisão será arredondado para 2 casas decimais e exibido como um número decimal.
consumo = kilometragem/volumeCombustivel
print(f"A taxa de consumo do veiculo é de {consumo:.2f} km/l")  

print("A taxa de consumo do veiculo é de {0:.2f} km/l".format(round(consumo, 2)))
#O método round() é usado para arredondar um número para um determinado número de casas decimais. No exemplo acima, round(consumo, 2) arredonda o valor da variável consumo para 2 casas decimais antes de formatá-lo na string. Isso é útil para garantir que o valor exibido seja mais legível e fácil de entender, especialmente quando se trata de números com muitas casas decimais.
