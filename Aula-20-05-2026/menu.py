'''Este modulo cria a funcao menu'''
import operacoes as op

def menu():
    '''Funcao para subir o menu'''
    while True:
        print('Obrigado por usar nossa calculadora super avançada :)! \n')

        print('Escolha uma das opções abaixo: \n')
        print('1 - Para Soma \n')
        print('2 - Para Subtração \n')
        print('3 - Para Multiplicação \n')
        print('4 - Para Divisão \n')
        print('5 - Para Calcular IMC \n')

        escolha = int(input("Digite aqui a sua opção: "))
        print('\n')

        match escolha:
            case 1:
                print('Você escolheu a operação de soma de dois números! \n')
                num1 = int(input("Digite aqui o primeiro número: "))
                num2 = int(input("Digite aqui o segundo número: "))
                resultado = op.somar(num1,num2)

                print(f'O resultado da soma de {num1} e {num2} é: {resultado}! \n')
                print('Foi um prazer ajudar!')
                break 
            case 2:
                print('Você escolheu a operação de subtração de dois números! \n')
                num1 = int(input("Digite aqui o primeiro número: "))
                num2 = int(input("Digite aqui o segundo número: "))
                resultado = op.subtrair(num1,num2)

                print(f'O resultado da subtração de {num1} e {num2} é: {resultado}! \n')
                print('Foi um prazer ajudar!')
                break    
            case 3:
                print('Você escolheu a operação de multiplicação de dois números! \n')
                num1 = int(input("Digite aqui o primeiro número: "))
                num2 = int(input("Digite aqui o segundo número: "))
                resultado = op.multiplicar(num1,num2)

                print(f'O resultado da multiplicação de {num1} e {num2} é: {resultado}! \n')
                print('Foi um prazer ajudar!')
                break
            case 4:
                print('Você escolheu a operação de divisão de dois números! \n')
                numerador = int(input("Digite aqui o numerador: "))
                denominador = int(input("Digite aqui o denominador: "))
                resultado = op.dividir(numerador,denominador)

                if resultado != 0:
                    print(f'O resultado da divisão de {numerador} por {denominador} é: {resultado}! \n')
                    print('Foi um prazer ajudar!')
                    break
                else:
                    print('\n')
                    #print(f"Não é possível dividir {numerador} por ZERO!")
                    print("Voltando ao menu principal...")
                    _ = input("Pressione qualquer tecla para continuar...")

            case 5:
                print('Você escolheu calcular o IMC! \n')
                peso = float(input("Digite aqui o peso: "))
                altura = float(input("Digite aqui a altura: "))
                resultado = op.calcular_imc(peso,altura)

                print(f'O indice IMC {peso} e {altura} é: {resultado}! \n')
                print('Foi um prazer ajudar!')
                break

            case _:
                print('Você escolheu uma opção incorreta!! \n')
                _ = input("Pressione qualquer tecla para continuar...")