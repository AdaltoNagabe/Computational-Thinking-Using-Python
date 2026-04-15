peso = float(input("Digite o peso: "))
altura = float(input("Digite a altura: "))
imc = peso / (altura ** 2)

if imc < 18.5:
    print("Seu IMC e: " + str(imc) + ". Esta abaixo do peso")
elif imc >= 25:
    print("Seu IMC e: " + str(imc) + ". Esta acima do peso")
else:
    print("Seu IMC e: " + str(imc) + ". Seu peso e normal")
