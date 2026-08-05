'''variavel global por isso esta em letras maiusculas'''
PI = 3.1314

'''funcao nome'''
def nomeProfessor():
    nome = input("Digite seu nome: ")

    '''tratamento de entrada, verifica se o usuario nao digitou nada e deu enter'''
    if nome:
        return nome
    else:
        return None

print("FORA DO TESTE!!!")

'''esse tipo de funcao "dunder name" somente executa dentro deste arquivo'''
'''estou chamando a funcao de main'''
if __name__ == "__main__":

    name = nomeProfessor()
    print(name)