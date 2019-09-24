import random
import math
import csv

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')



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

def main():
    xs_array = []
    ys_array = []
    zs_array = []
    # Inicializando constantes
    c1 = 1
    c2 = 1
    w = 0.72

    # Tornar parametrizado
    numero_particulas = 100
    numero_posicao_particula = 2
    iteracoes = 50
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

            

        '''for gb in global_best:
                xs = gb.posicao[0]
                ys = gb.posicao[1]
                zs = gb.fit
                
                xs_array.append(xs)
                ys_array.append(ys)
                zs_array.append(zs)'''
        
            
        '''textoX = ''
        textoY = ''
        for gb in global_best:
            textoX =  textoX + str(gb.posicao[0]) + ', '
            textoY = textoY + str(gb.posicao[1]) + ', '

        # print(textoX)
        arq = open('global_20_50.csv', 'a')
        # arq.write('\n')
        arq.write('\nX, ' + textoX + '\nY, ' + textoY) 
        arq.close()'''

        
        global_geral.append(ordenado[0])    
        loop = loop + 1
        
        



    '''ax.scatter(xs_array, ys_array, zs_array, zdir='z', s=20,
                                   c=None, depthshade=True)

    ax.set_xlabel('X Label ')
    ax.set_ylabel('Y Label ')
    ax.set_zlabel('Z Label ')
    print(ordenado[0].fit)

                    
    plt.show()'''

    c = open("teste.csv", "a")
    c.write("Melhor" +", " +"Média Interações" + "\n")

    aux = 0


    for i in range(0, len(global_todas_iteracoes)):
        #print(global_geral[i].fit)
        

        for j in range(0, len(global_todas_iteracoes[i])):

            aux = aux + global_todas_iteracoes[i][j].fit

        #print(aux/iteracoes)


        linha = str(global_geral[i].fit) + " ," + str(aux/iteracoes) + "\n"
        c.write(linha)

    print(len(global_geral))


main()
