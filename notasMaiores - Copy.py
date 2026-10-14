import json
 
 
with open("filmes.json", "r", encoding="utf-8") as arquivo:
    raw = arquivo.read()
 
leitura = json.loads(raw)
 
#print(leitura)
 
listaNotasMaiores = []
 
for film in leitura:
    if film["notaImdb"] >= 9.0:
        listaNotasMaiores.append(film)
 
 
print(listaNotasMaiores)


with open("filmes.json", "x", encoding="utf-8") as arquivo:
    escritor = json.dumps(listaNotasMaiores,indent=4)
    arquivo.write()