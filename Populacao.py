from Pessoa import Pessoa
import numpy as np
from random import *

'''
Um algoritmo para para gerar populaçoes de tamanho arbitrario, que apresentem as mesmas
estatisticas da amostra da PNAD, com respeito a media e coeficiente de variaçao.
'''


# Esta função recebe a porcentagem de pessoas em cada categoria e a população.
# E ela retorna o a quantidade de pessoas em cada categoria.
def fun(a, w):
    t = sum(a)
    b = np.zeros(len(a))
    c = np.zeros(len(a))
    for k in range(len(a)):
        b[k] = (a[k] / t)
    for o in range(len(a)):
        for d in range(len(a) - o - 1):
            b[len(a) - o - 1] += b[d]
    for m in range(w):
        z = random()
        if z <= b[0]:
            c[0] += 1
        else:
            for n in range(1, len(a)):
                if b[n - 1] < z <= b[n]:
                    c[n] += 1
    return c


class Populacao:
    def __init__(self, tamanho=1000):
        self.tamanho = tamanho

        # lista das porcentagens de pessoas em cada categoria
        porcentagem = np.array([[.023, .065, .108, .244, .348, .126, .031, .055], [.22, .78],
                                [.822, .178], [.562, .438], [.577, .423]])
        # CV de cada categoria
        dv = np.array([[.241, .133, .109, .069, .055, .104, .225, .170], [.081, .023],
                       [.018, .083], [.032, .042], [.033, .044]])

        faixas = np.array([[0, 0, 0, 0, 0, 0, 0], [0, 0], [0, 0], [0, 0], [0, 0]])
        cat = np.array([[0, 0, 0, 0, 0, 0, 0], [0, 0], [0, 0], [0, 0], [0, 0]])

        # cálculo do desvio padrão
        for u in range(5):
            v = dv[u]
            v = np.array(v)
            r = porcentagem[u]
            r = np.array(r)
            dv[u] = r * v
        for q in range(5):
            v = dv[q]
            v = np.array(v)
            e = uniform(-1, 1)
            for i in range(len(v)):
                v[i] = v[i] * e
            r = porcentagem[q]
            r = np.array(r)
            faixas[q] = r + v

        # retorno da função fun
        c = 0
        for j in faixas:
            cat[c] = fun(j, tamanho)
            c += 1

        # lista com informações para instancair pessoas
        popfin = np.zeros((tamanho, 5))

        # criando essa lista popfin
        inicio = np.array(list(range(tamanho)))
        np.random.shuffle(inicio)
        d = 0
        for i in range(len(cat)):
            p = 0
            for j in range(len(cat[i])):
                for k in range(p, int(cat[i][j]) + p):
                    popfin[inicio[k], i] = j
                p += int(cat[i][j])

        # indivíduos da população
        self.individuos = [Pessoa(g) for g in popfin]

    def amostra(self, n):
        pop = np.random.choice(self.individuos, n)
        return pop
