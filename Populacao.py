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



class Populacao:
    def __init__(self, tamanho=1000):
        self.tamanho = tamanho
        self.individuos = []
        cat=np.array([[], [], [], [], []])

        porcentagem = np.array([[2.3, 6.5, 10.8, 24.4, 34.8, 12.6, 3.1, 5.5], [], [], [], []])*(1/100)  # lista das porcentagens de pessoas em cada categoria
        dv = np.array([[], [], [], [],[]])*(1/100) # desvio padrao de cada categoria
        faixas = np.array([[], [], [], [], []])
        for u in range(5):
            v=dv[u]
            v=np.array(v)
            r=porcentagem[u]
            r=np.array(r)
            dv[u]=r*v
        for q in range(5):
            v=dv[q]
            v=np.array(v)
            e=random.uniform(-1,1)
            v=v*e
            r=porcentagem[q]
            r=np.array[r]
            faixas[q]=r+v
        c=0
        for j in faixas:
            cat[c] = fun(j,tamanho)
            c += 1
        
        popfin = np.zeros((tamanho,5))
        inicio = np.array(list(range(tamanho)))
        np.random.shuffle(inicio)
        d=0
        for i in cat:
            ind3 = cat.index(i)
            p = 0
            for j in range(len(i)):
                if j==0:
                else:
                    p += i[j-1]
                    for k in range(p,i[j]+p):
                        popfin[inicio[k],ind3] = j
        
                
        self.individuos = [Pessoas(g) for g in popfin]
            
        atributos = [['de 0 a 1 ', 'mulher']]

    def amostra(self, n):
        amostrapop = np.random.choice(self.individuos, n)
        return amostrapop
