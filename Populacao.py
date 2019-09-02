from Pessoa import Pessoa


'''
Um algoritmo para para gerar populaçoes de tamanho arbitrario, que apresentem as mesmas
estatisticas da amostra da PNAD, com respeito a media e coeficiente de variaçao.
'''


class Populaçao:
    def __init__(self, tamanho=1000):
        self.tamanho = tamanho
        self.individuos = []

    def amostra(self, n):
        pass
