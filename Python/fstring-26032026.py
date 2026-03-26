nome = "adalto"
idade = 36
print(f"Meu nome é {nome.title()} e minha idade é {idade} anos.")
#fstring é uma forma de formatar strings em Python, onde você pode incluir expressões dentro de chaves {} que serão avaliadas e inseridas na string resultante. No exemplo acima, usamos f-string para criar uma mensagem que inclui o nome e a idade de uma pessoa. O método .title() é usado para capitalizar a primeira letra do nome.

#.format
print("Meu nome é {} e minha idade é {} anos.".format(nome, idade))
#O método .format() é outra forma de formatar strings em Python. Ele permite que você insira valores em uma string usando chaves {} como marcadores de posição. No exemplo acima, as chaves {} serão substituídas pelos valores fornecidos na ordem em que aparecem. Para usar o método .format(), você precisa passar os valores como argumentos para o método, por exemplo: "Meu nome é {} e minha idade é {} anos.".format(nome, idade).

print("Meu nome é {0} e minha idade é {1} anos.".format(nome, idade))
#Você também pode usar índices dentro das chaves {} para especificar a ordem dos argumentos. No exemplo acima, {0} se refere ao primeiro argumento (nome) e {1} se refere ao segundo argumento (idade). Isso é útil quando você deseja reutilizar os mesmos valores em diferentes partes da string ou quando deseja alterar a ordem dos argumentos sem precisar alterar a ordem dos marcadores de posição.

