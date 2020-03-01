
class Carro():
    qte_carros = 0

    def __init__(self, ano = '', cor = '', quilometragem = '', marca = ''):
        self.ano = ano
        self.cor = cor
        self.quilometragem = quilometragem
        self.marca = marca

        Carro.qte_carros += 1

    def set_ano(self, ano):
        self.ano = ano

    def set_cor(self, cor):
        self.cor = cor

    def set_km(self, quilometragem):
        self.quilometragem = int(quilometragem)

    def set_marca(self, marca):
        self.marca = marca

    def to_dict(self):
        return {'Cor': self.cor, 'Quilometragem': self.quilometragem, 'Marca': self.marca, 'Ano': self.ano }
        