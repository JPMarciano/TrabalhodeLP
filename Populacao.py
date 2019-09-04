from Pessoa import Pessoa
from random import uniform
import numpy as np

'''
Um algoritmo para para gerar populaçoes de tamanho arbitrario, que apresentem as mesmas
estatisticas da amostra da PNAD, com respeito a media e coeficiente de variaçao.
'''

class Populacao:
    def __init__(self, tamanho=1000):
        self.tamanho = tamanho
        self.individuos = []

        porcentagem = (1/100)*[[2.3, 6.5, 10.8, 24.4, 34.8, 12.6, 3.1, 5.5], [], [], [], []]  # lista das porcentagens de pessoas em cada categoria
        dv = [[], [], [], [], []]  # desvio padrao de cada categoria
        faixas = [[], [], [], [], []]



    def amostra(self, n):
        amostrapop = np.random.choice(self.individuos, n)
        return amostrapop
