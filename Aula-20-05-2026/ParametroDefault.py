def dividirPorDezouNao(numerador:float, denominador:float = 10) -> float:
    divisao = numerador/denominador
    return divisao

print(dividirPorDezouNao(2)) #divide 2 por 10
print(dividirPorDezouNao(2,100)) #se eu declarar o denominador ele sobrepoe o default


def conectar_banco(usuario: str, host: str = "localhost", porta: int = 3306) -> str:
    return f"conectando como {usuario} em {host}:{porta}"
