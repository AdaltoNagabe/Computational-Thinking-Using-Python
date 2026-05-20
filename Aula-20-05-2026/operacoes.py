PI = 3.1415

def somar(num1:float,num2:float) -> float: #utilizando o typehinting
    return num1+num2

def subtrair(num1,num2):
    return num1-num2

def multiplicar(num1,num2):
    return num1*num2

def dividir(numerador,denominador:float = 10) -> float:
    if denominador != 0:
        return numerador/denominador
    else:
        print('\n')
        print(f"Não é possível dividir {numerador} por ZERO!")
        return 0
    
def calcular_imc(peso:float, altura:float) -> float:
    return peso / (altura ** 2)
    