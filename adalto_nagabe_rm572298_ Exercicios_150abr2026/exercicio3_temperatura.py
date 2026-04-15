temperatura = float(input("Entre com a temperatura atual: "))
if temperatura > 25:
    print("Alerta! Temperatura esta em: " + str(temperatura) + " graus. Acima do limite permitido")
else:
    print("Temperatura esta em: " + str(temperatura) + " graus. OPERACAO NORMAL")