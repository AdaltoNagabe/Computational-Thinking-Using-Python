a = int(input("Entre com os dias do projeto A: "))
b = int(input("Entre com os dias do projeto B: "))
c = int(input("Entre com os dias do projeto C: "))
if a < 0 or b < 0 or c < 0:
    print("Os dias nao podem ser negativos")
else:
    diasTotais = a + b + c
    print("O tempo total do projeto em dias sao: " + str(diasTotais))