#Exercicio 3 - Atribuindo valores a 4 tipos de variáveis
faculdade = "FIAP"
idade = "57"
altura = 1.70
estudante = True

#Item A - Atribuindo 5 numeros inteiros de 0 a 10
cp1 = 10
cp2 = 7
sprint1 = 8
sprint2 = 7
gs1 = 6

#Item B - Atribuindo 4 variaveis (ponto flutuante)
mediaCps = (cp1 + cp2) / 2
mediaSprints = (sprint1 + sprint2) / 2
mediaGs = gs1
mediaFinal=((mediaCps * 0.2) + (mediaSprints * 0.2) + (mediaGs * 0.6))
           
#Item C - Atribuindo 2 strings (nome e sobrenome)
nome = "Adalto"
sobrenome = "Nagabe"

#Item D - Atribuindo 2 variaveis booleanas (Aprovado e Reprovado)
aprovado = True
reprovado = False

#Exercicio 4 - Operacoes basicas aritmeticas
#Item A - Soma de variaveis CPs e Sprints
somaCps = cp1 + cp2
somaSprints = sprint1 + sprint2

#Item B - Divisao de variaveis CPs e Sprints para obter a media
mediaCps = (cp1 + cp2) / 2
mediaSprints = (sprint1 + sprint2) / 2

#Iem C - Multiplicacao da media dos CPs por 0.2, a media dos Sprints por 0.2 e a media dos GS por 0.6
notaCps = mediaCps * 0.2
notaSprints = mediaSprints * 0.2
notaGs = mediaGs * 0.6

#Item D - Soma das notas dos CPs, Sprints e GS para obter a nota final
notaFinal = notaCps + notaSprints + notaGs

#Item E - Subtracao para verificar quanto falta para chegar a 6
mediaAprovacao = 6
faltaParaPassar = mediaAprovacao - notaFinal

#Exercicio 5 - Input de nota pelo terminal
notaInput = input("Digite o valor 9.1: ")

#Exercicio 6 - Operadores logicos
#Item A - Comparar nota final com a media de aprovacao
passou = notaFinal >= mediaAprovacao
    
#Iem B - Comparar e a nota final e diferente do input
comparaNotaInput = notaFinal != notaInput

#Exercicio 7
print("Nota Final: " + str(notaFinal))
print("O aluno " + nome + " " + sobrenome + " passou? " + str(passou))









