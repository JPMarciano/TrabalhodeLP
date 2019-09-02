from Pessoa import Pessoa
import numpy as np

'''
Um algoritmo para para gerar populaçoes de tamanho arbitrario, que apresentem as mesmas
estatisticas da amostra da PNAD, com respeito a media e coeficiente de variaçao.
'''


class Populacao:
    def __init__(self, tamanho=1000):
        self.tamanho = tamanho
        self.individuos = []

    def amostra(self, n):
        amostrapop = np.random.choice(self.individuos, n)
        return amostrapop
