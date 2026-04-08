nota1 = float(input("Digite a nota1: "))
nota2 = float(input("Digite a nota2: "))
foiPegoColando =input("Foi pego colando? ")
foiPegoColando = foiPegoColando.lower()

if foiPegoColando == "sim":
    nota1,nota2 = (0,0)

media = (nota1 + nota1) / 2

print("A media e: ",media)