luz = float(input("Despesa com energia eletrica: "))
agua = float(input("Despesa com agua: "))
alimentacao = float(input("Despesa com alimentacao: "))
aluguel = float(input("Despesa com aluguel: "))
limiteGasto = 3000

gastoTotal = luz + agua + alimentacao + aluguel

if gastoTotal > limiteGasto:
    print("Atenção! Seus gastos sao: " + str(gastoTotal) + ". Voce ultrapassou o limite estabelecido")
else:
    print("Seus gastos sao: " + str(gastoTotal) + ". Voce esta no limite estabelecido")