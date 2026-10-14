import json

with open("Teste.json","r",encoding="utf-8") as arquivo:
    leitor = arquivo.read()
    jayson = json.loads(leitor)

print(type(jayson))
print(jayson)
print("-" * 90)
print(leitor)
print("-" * 90)
print(jayson[0]["paciente"])