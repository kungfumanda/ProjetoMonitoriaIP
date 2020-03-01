'''Percorre os arquivos de teste e os devolve numa lista de carros'''

import os
from carro import Carro
import glob


def ler_arquivos_teste():
    testes = []
    folder = r'./'
    for arquive in glob.glob('./test*.*'):
        fp = os.path.join(folder, arquive)
        with open(fp, "r", encoding="utf8") as infile:
            testes.append(infile.read())
    return testes



def organizar_entradas():
    testes = ler_arquivos_teste()
    catalogo = []
    for c in range(len(testes)):
        catalogo.append('')

    for i in range(len(testes)):
        catalogo[i] = Carro()
        aux = testes[i].split('\n')
        if aux[0].lower() != "categoria":
            catalogo[i].set_marca(aux[0].split()[0])
        for a in range(len(aux)):
            if aux[a].lower() == "marca":
                catalogo[i].set_marca(aux[a+1].replace("GM - ", "").title())
            elif aux[a].lower() == "quilometragem" or aux[a].lower() == "km":
                catalogo[i].set_km(str(aux[a + 1]))
            elif aux[a].lower() == "cor":
                catalogo[i].set_cor(aux[a + 1])
            elif aux[a].lower() == "ano":
                catalogo[i].set_ano(' '.join(str(aux[a + 1]).split()))
    return catalogo







