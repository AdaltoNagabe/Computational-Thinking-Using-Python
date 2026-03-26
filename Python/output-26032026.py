#output e a saida. Na pratica nao existe no python uma funcao chamada output, o que existe e a funcao print, que e utilizada para imprimir algo na tela, ou seja, para gerar uma saida. O print pode receber varios argumentos, separados por virgula, e vai imprimir todos eles na tela, separados por um espaco. O print tambem pode receber um argumento chamado end, que define o que vai ser impresso no final da linha, por padrao o end e um espaco, mas pode ser alterado para qualquer coisa, como por exemplo uma quebra de linha (\n) ou uma tabulacao (\t).
print("Hello World") #imprime Hello World na tela
print("Hello", "World") #imprime Hello World na tela, separado por um espaco
print("Hello", "World", end="\n") #imprime Hello World na tela, separado por um espaco e depois quebra a linha
print("Hello", "World", end="\t") #imprime Hello World na tela, separado por um espaco e depois tabula a linha  
print("Hello World")