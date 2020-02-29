
class Carro():
    qte_carros = 0

    def __init__(self):
        self.ano = ''
        self.cor = ''
        self.quilometragem = ''
        self.marca = ''

        Carro.qte_carros += 1

    def set_ano(self, ano):
        self.ano = ano

    def set_cor(self, cor):
        self.cor = cor

    def set_km(self, quilometragem):
        self.quilometragem = quilometragem

    def set_marca(self, marca):
        self.marca = marca