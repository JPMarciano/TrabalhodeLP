from Pessoa import Pessoa
from random import uniform
import numpy as np
from random import *
'''
Um algoritmo para para gerar populaçoes de tamanho arbitrario, que apresentem as mesmas
estatisticas da amostra da PNAD, com respeito a media e coeficiente de variaçao.
'''
def fun(a,k):
    t=sum(a)
    b=[]
    c=a
    for k in len(a):
        b=b.append(a[k]/t)
    for m in range(k)
        z=random()
            if z<=b[0]:
            c[0]+=1    
        for n in range(1,len(a)):
            if z<=b[n] and z>=b[n-1]:
                c[n]+=1
    return c


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
