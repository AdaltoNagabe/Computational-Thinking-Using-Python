def calcular_imc(peso:float, altura:float) -> float:
    calcular_imc = peso/(altura**2)
    return calcular_imc

print(calcular_imc(peso='100', altura=1.76))