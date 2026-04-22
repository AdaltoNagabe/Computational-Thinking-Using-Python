nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

VetorNotas = [nota1,nota2,nota3]
print ("As notas sao: " + str(VetorNotas))

VetorNotas.sort(reverse=True)
media = (VetorNotas[0] + VetorNotas[1]) /2
print ("A media das duas maiores e: " + str(media))