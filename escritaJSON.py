import json
from textwrap import indent

novoRegistro = {
        "Id": 3,
        "paciente": "Jose Maciel",
        "medico": "Dr. Dario Nery",
        "data": "2024-10-15",
        "hora": "13:30",
        "especialidade": "Clinico Geral"
    }

with open("Teste2.json","x",encoding="utf-8") as arquivo:
    lista = []
    lista.append(novoRegistro)

    escritor = json.dumps(lista,indent=4)
    arquivo.write(escritor)