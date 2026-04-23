# E um metodo que serve para concatenar duas listas, ou seja, para adicionar os elementos de uma lista a outra lista. O método extend recebe como parâmetro a lista que deve ser concatenada com a lista original. O método extend é diferente do operador +, pois o operador + cria uma nova lista com os elementos das duas listas, enquanto o método extend modifica a lista original adicionando os elementos da outra lista. O código abaixo mostra um exemplo de como usar o método extend para concatenar duas listas:
# E um metodo perigoso, pois ele modifica a lista original, ou seja, a lista original é modificada para conter os elementos da outra lista. Por isso, é importante ter cuidado ao usar o método extend, pois ele pode causar problemas se a lista original for usada em outras partes do código. O código abaixo mostra um exemplo de como usar o método extend para concatenar duas listas:

notasSemestre1 = [7.5, 8.0, 6.0, 9.0, 10.0]
notasSemestre2 = [8.5, 9.0, 7.0, 6.5, 8.0]

#Concatenou as notas dos dois semestres em uma única lista usando o operador +, ou seja, a lista notasSemestre1 agora contém os elementos [7.5, 8.0, 6.0, 9.0, 10.0, 8.5, 9.0, 7.0, 6.5, 8.0]
notasSemestre1.extend(notasSemestre2) #O método extend é usado para adicionar os elementos de uma lista a outra lista. No caso, os elementos da lista notasSemestre2 são adicionados à lista notasSemestre1, e a lista notasSemestre1 agora contém os elementos [7.5, 8.0, 6.0, 9.0, 10.0, 8.5, 9.0, 7.0, 6.5, 8.0]
print(notasSemestre1)

