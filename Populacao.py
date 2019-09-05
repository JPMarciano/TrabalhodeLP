from Pessoa import Pessoa
from random import uniform
import numpy as np
from random import *
'''
Um algoritmo para para gerar populaçoes de tamanho arbitrario, que apresentem as mesmas
estatisticas da amostra da PNAD, com respeito a media e coeficiente de variaçao.
'''
def fun(a, w):
    t = sum(a)
    b = np.zeros(len(a))
    c = np.zeros(len(a))
    for k in range(len(a)):
        b[k] = (a[k]/t)
    for o in range(len(a)):
        for d in range(len(a)-o-1):
          b[len(a)-o-1] += b[d]
    for m in range(w):
        z = random()
        if z <= b[0]:
            c[0] += 1
        else:
          for n in range(1, len(a)):
            if b[n-1] < z <= b[n]:
                c[n] += 1
    return c
print(fun([2,3,4,1,50,20,10,10],1000))



class Populacao:
    def __init__(self, tamanho=1000):
        self.tamanho = tamanho
        self.individuos = []

        porcentagem = (1/100)*[[2.3, 6.5, 10.8, 24.4, 34.8, 12.6, 3.1, 5.5], [], [], [], []]  # lista das porcentagens de pessoas em cada categoria
        dv = [[], [], [], []]  # desvio padrao de cada categoria
        faixas = [[], [], [], [], []]
        atributos = [['de 0 a 1 ', 'mulher']]

    def amostra(self, n):
        amostrapop = np.random.choice(self.individuos, n)
        return amostrapop
