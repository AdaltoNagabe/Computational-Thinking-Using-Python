nomes = ['adalto','massashiro']
medias = [7.5,6]

def processar_notas(nomes: list[str], medias:list[float]) -> list[tuple]:
    boletim = []
    for i in range(len(nomes)):
        boletim.append((nomes[i],medias[i]))
    return boletim

print (boletim)