import random
import math
import csv

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 
import numpy as np


class Particula:
    def __init__(self, posicao, velocidade, fit, pBest):
        self.posicao = posicao
        self.velocidade = velocidade
        self.fit = fit
        self.pBest = pBest
        
    def get_fitness(self):
        return self.fit


# Funções
def cria_particula(numero_particulas):
    enxame = [Particula(0, 1, 2, 3) for x in range(0, numero_particulas)]
    return enxame


def inicializa_posicao(enxame, numero_posicao_particula):
    for particula in enxame:

        posicao_particula = [random.uniform(-512, 512)
                             for j in range(0, numero_posicao_particula)]
        # print(posicao_particula)
        particula.posicao = posicao_particula


def inicializa_velocidade(enxame, numero_posicao_particula):
    for particula in enxame:

        velocidade_particula = [
            random.uniform(-77, 77) for j in range(0, numero_posicao_particula)]
        particula.velocidade = velocidade_particula


def fitness(posicao):
    return (- (posicao[1] + 47) * math.sin(math.sqrt(math.fabs((posicao[0] / 2) + (posicao[1] + 47))))) - (posicao[0] * math.sin(math.sqrt(math.fabs(posicao[0] - (posicao[1] + 47)))))


def pBest(particula,fitness):

    if (particula.fit > fitness):
        particula.fit = fitness
        particula.pBest = particula

def imprime_enxame(enxame):

    for particula in enxame:
        print(particula.posicao, particula.fit)
    print("\n")

def menor(particula):
    return (particula[0])

def escreveArq(c, global_todas_iteracoes, global_geral, iteracoes):
    
    lst_media_gb = []
    lst_gb = []
    for i in range(0, len(global_todas_iteracoes)):
        aux = 0
        for j in range(0, len(global_todas_iteracoes[i])):
            aux = aux + global_todas_iteracoes[i][j].fit

        lst_media_gb.append(aux/iteracoes)

        lst_gb.append(global_geral[i].fit)

        linha = str(i+1)+" E"+ ","+ str(global_geral[i].fit) + " ," + str(aux/iteracoes) + "\n"
        c.write(linha)

    c.write("\n\n")
        
    return lst_media_gb, lst_gb

def main():
    # Inicializando constantes
    c1 = 2.05
    c2 = 2.05
    w = 0.72

    # Tornar parametrizado


    numero_particulas = 50
    numero_posicao_particula = 2
    iteracoes = 20
    vezes = 10
    loop = 0

    #melhor gbest de cada execucao
    global_geral = []

    #todos gbest

    global_todas_iteracoes = []

    while (loop < vezes):
        
        global_best = []

        # Criando as particulas
        enxame = cria_particula(numero_particulas)

        # Inicializando a posição de cada particula
        inicializa_posicao(enxame, numero_posicao_particula)

        # Inicializando a velocidade | deslocamento de cada particula
        # Nesse primeiro momento todas as particulas terão a mesma velocidade | deslocamento
        inicializa_velocidade(enxame, numero_posicao_particula)

    #   -----------
    
        for i in range(0,iteracoes):
            fit = 0
            for particula in enxame:

                # Calculando Fitness
                fit = fitness(particula.posicao)

                # Calculando o pBest
                if (particula.pBest == 3):
                    particula.fit = fit
                    particula.pBest = particula
                else:
                    pBest(particula,fit)

        
            # Descobrindo o gBest
            ordenado = sorted(enxame, key=Particula.get_fitness)
            global_best.append(ordenado[0])

            for particula in enxame:

                for i in range(0, len(particula.velocidade)):
                    # Calcula a velocidade
                    veloz = (w * particula.velocidade[i]) + (c1 * random.random() * (particula.pBest.posicao[i] - particula.posicao[i])) + (c2 * random.random() * (global_best[len(global_best)-1].posicao[i] - particula.posicao[i]))
                    
                    if (veloz > 77):
                        veloz = 77
                    if (veloz < -77):
                        veloz = -77
                    particula.velocidade[i] = veloz

                    # Calcula a posicão
                    nova_posicao = 0
                    nova_posicao = particula.posicao[i] + particula.velocidade[i]

                    if(nova_posicao > 512):
                        particula.posicao[i] = 512
                        particula.velocidade[i] = 0.0
                    elif(nova_posicao < -512):
                        particula.posicao[i] = -512
                        particula.velocidade[i] = 0.0
                    else:
                        particula.posicao[i] = nova_posicao

        global_todas_iteracoes.append(ordenado)
        global_geral.append(ordenado[0])    
        loop = loop + 1
        

    c = open("teste.csv", "a")
    
    c.write(str(iteracoes)+" I - "+str(numero_particulas)+" P " + ", "+"Melhor" +", " +"Média Interações" + "\n")

    lst_media_gb = []
    lst_gb = []

    lst_media_gb, lst_gb = escreveArq(c, global_todas_iteracoes, global_geral, iteracoes)

    c.close()

    print("gb: ", lst_gb)
    print()
    print("media gb: ",lst_media_gb)
    

    #plotar grafico
    x = [1,2,3,4,5,6,7,8,9,10] #execucoes

    plt.plot(x, lst_gb, 'go')
    plt.plot(x, lst_gb, 'k:', color='orange', label='GBest')
    
    plt.plot(x, lst_media_gb, 'r^',)
    plt.plot(x, lst_media_gb, 'k--', color='blue', label='Média Gbest')

    plt.title(str(iteracoes)+" Interações - "+str(numero_particulas)+" Partículas")

    plt.grid(True)
    plt.xlabel("Execuções")
    plt.legend(loc=0)
    plt.show()

#global_best = melhores gb de cada execucao
#lista_media_gb = media de todos os gb de uma execucao


main()
