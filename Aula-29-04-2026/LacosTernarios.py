# se e ou nao azul

varIdade = input("Digite a sua idade: ")
varIdade = int(varIdade)

if varIdade >=18:
    print("Azul")
else:
    print("Nao e azul")

print("Azul" if varIdade >=18 else "Nao e azul") #esta linha substitui o bloco IfElse acima (operador ternario). Nao aceita elif