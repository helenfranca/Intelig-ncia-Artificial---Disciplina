import random
import math


class Particula:
    def __init__(self, posicao, velocidade, fit, pBest):
        self.posicao = posicao
        self.velocidade = velocidade
        self.fit = fit
        self.pBest = pBest


# Funções
def fitness(posicao):
    return (- (posicao[1] + 47) * math.sin(math.sqrt(math.fabs((posicao[0] / 2) + (posicao[1] + 47))))) - (posicao[0] * math.sin(math.sqrt(math.fabs(posicao[0] - (posicao[1] + 47)))))


def gBest(enxame):
    menor = Particula([512, 512], 0, 1, 0)

    for particula in enxame:
        if (particula.posicao[0] < menor.posicao[0]) and (particula.posicao[1] < menor.posicao[1]):
            menor = particula

    return menor


def pBest(particula):

    if (particula.posicao[0] < particula.pBest.posicao[0]) and (particula.posicao[1] < particula.pBest.posicao[1]):
        particula.pBest.posicao[0] = particula.posicao[0]
        particula.pBest.posicao[1] = particula.posicao[1]


def cria_particula(numero_particulas):
    enxame = [Particula(0, 1, 2, 3) for x in range(0, numero_particulas)]
    return enxame


def inicializa_posicao(enxame, numero_posicao_particula):
    for particula in enxame:

        posicao_particula = [random.uniform(-512, 512)
                             for j in range(0, numero_posicao_particula)]
        particula.posicao = posicao_particula


def inicializa_velocidade(enxame, numero_posicao_particula):
    for particula in enxame:

        velocidade_particula = [
            random.uniform(-77, 77) for j in range(0, numero_posicao_particula)]
        particula.velocidade = velocidade_particula


def imprime_enxame(enxame):
    for particula in enxame:
        print(particula.posicao, particula.velocidade)


def main():

    # Inicializando constantes
    c1 = 1.0
    c2 = 1.0
    w = 0.72

    global_best = []

    # Tornar parametrizado
    numero_particulas = 20
    numero_posicao_particula = 2

    # Criando as particulas
    enxame = cria_particula(numero_particulas)

    # Inicializando a posição de cada particula
    inicializa_posicao(enxame, numero_posicao_particula)

    # Inicializando a velocidade | deslocamento de cada particula
    # Nesse primeiro momento todas as particulas terão a mesma velocidade | deslocamento
    inicializa_velocidade(enxame, numero_posicao_particula)

    #   -----------

    for particula in enxame:

        # Calculando Fitness
        particula.fit = fitness(particula.posicao)

        # PBest | No momento o melhor é a posição atual porque é a primeira.
        # Não houve outra pra que pudesse ser comparada
        if (particula.pBest == 3):
            particula.pBest = particula
        else:
            pBest(particula)

    # Descobrindo o gBest
    global_best.append(gBest(enxame))

    # Calcula a velocidade
    for particula in enxame:

        for i in range(0, len(particula.velocidade)):

            veloz = (w * particula.velocidade[i]) + (c1 * random.random() * (particula.pBest.posicao[i] - particula.posicao[i])) + (
                c2 * random.random() * (global_best[len(global_best)-1].posicao[i] - particula.posicao[i]))

            if (veloz > 77):
                veloz = 77
            if (veloz < -77):
                veloz = -77

            particula.velocidade[i] = veloz

    # Calcula a posicão
    for particula in enxame:
        nova_posicao = 0
        for i in range(0, len(particula.posicao)):
            nova_posicao = particula.posicao[i] + particula.velocidade[i]

            if(nova_posicao > 512):
                particula.posicao[i] = 512
                particula.velocidade[i] = 0
            elif(nova_posicao < -512):
                particula.posicao[i] = -512
                particula.velocidade[i] = 0
            else:
                particula.posicao[i] = nova_posicao

    imprime_enxame(enxame)


main()
