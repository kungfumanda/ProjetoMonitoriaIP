import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import leitor_arquivos
from carro import Carro

'''dados arquivos nomeados como test*.txt, o programa os organiza numa lista de carros a venda'''

catalogo = leitor_arquivos.organizar_entradas()
tabela = pd.DataFrame.from_records([s.to_dict() for s in catalogo])


'''grafico que mostra a quantidade de carros de cada cor no catálogo'''
y = tabela['Cor'].value_counts()
labels = y.index.tolist()
y.plot(kind = 'pie', y = 'Cor', labels = labels, explode = (0.1, 0, 0, 0), legend = True, colors= ['white', 'black', 'silver', 'blue'], shadow = True, startangle = 140, autopct='%1.1f%%' )
plt.axis('equal')
plt.title('Percentual de cores de carros no catálogo')
plt.savefig('grafico1.png')
plt.close()

'''grafico que mostra quilometragem média que as marcas atingem antes que os donos queiram vender seus carros'''
aux1 = tabela.groupby(by=['Marca']).mean()
aux1.plot(color = 'purple', figsize = (8, 8), linestyle = "-.")
plt.title('Quilometragem média por veículo antes da venda')
plt.savefig('grafico2.png')
plt.close()

'''grafico que mostra a quantidade de carros no catalogo por marca'''
x = tabela['Marca'].value_counts()
x.plot(kind = 'bar', color = 'red', figsize = (8,8))
plt.title('Quantidade de veículos por marca')
plt.savefig('grafico3.png')
plt.close()

'''grafico que mostra a relação entre quilometragem e ano de lançamento'''
aux = tabela.sort_values(['Ano', 'Quilometragem'])
plt.plot(aux['Quilometragem'], aux['Ano'] , color = 'green', linestyle = ":")
plt.title('Relação entre ano de lançamento e quilometragem')
plt.ylabel('Ano')
plt.xlabel('Quilometragem')
plt.savefig('grafico4.png')
plt.close()


