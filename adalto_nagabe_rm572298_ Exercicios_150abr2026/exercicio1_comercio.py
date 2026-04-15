banana = int(input("Digite a quantidade de bananas vendidas: "))
masan = int(input("Digite a quantidade de macas vendidas: "))
if banana > masan:
    print("As bananas tiveram mais vendas!")
elif banana < masan:
    print("As macas tiveram mais vendas!")
else:
    print("Houve um empate nas vendas de macas e bananas")