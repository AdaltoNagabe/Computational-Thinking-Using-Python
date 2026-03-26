#login utilizando o input
usuario = input("Digite seu nome de usuário: ")
senha = input("Digite sua senha: ")
print("Usuário: ", usuario)
print("Senha: ", senha)

#O UNDERSCORE e uma variavel descartavel. Deppois e utilizada nao serve mais pra nada
#o codigo abaixo e um exemplo de como utilizar o underscore para descartar o valor do input
#o programa vai esperar o usuario digitar algo e depois vai descartar o valor digitado, ou seja, nao vai ser armazenado em nenhuma variavel
_ = input("Pressione Enter para continuar...")

_,a = [1, 2]
print(a)

#evaluation do input, o eval vai tentar avaliar o que o usuario digitou, se for um numero ele vai ser convertido para numero, se for uma string ele vai ser convertido para string, se for uma expressao matematica ele vai ser avaliada e o resultado vai ser retornado
evalTest = eval(input("Digite qualquer coisa que eu vou adivinhar!!! "))
print(type(evalTest))


