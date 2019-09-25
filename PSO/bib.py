import Particula
import random
import math

# Funções


def cria_particula(numero_particulas):
    enxame = [Particula.Particula(0, 1, 2, 3)
              for x in range(0, numero_particulas)]
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


def velocidade(w, particula, i, c1, c2, global_best):
    veloz = (w * particula.velocidade[i]) + (c1 * random.uniform(0, 1) * (particula.pBest.posicao[i] - particula.posicao[i])) + (
        c2 * random.uniform(0, 1) * (global_best[len(global_best)-1].posicao[i] - particula.posicao[i]))

    if (veloz > 77):
        veloz = 77
    if (veloz < -77):
        veloz = -77

    return veloz


def calcula_posicao(particula, i):
    nova_posicao = 0
    nova_posicao = particula.posicao[i] + \
        particula.velocidade[i]

    if(nova_posicao > 512):
        particula.posicao[i] = 512
        particula.velocidade[i] = 0.0
    elif(nova_posicao < -512):
        particula.posicao[i] = -512
        particula.velocidade[i] = 0.0
    else:
        particula.posicao[i] = nova_posicao


def pBest(particula, fitness):

    if (particula.pBest == 3):
        particula.fit = fitness
        particula.pBest = particula
    elif (particula.fit > fitness):
        particula.fit = fitness
        particula.pBest = particula


def escreve_arquivo(texto, iteracoes, numero_particulas):
    arquivo = open(str(iteracoes)+'_' + str(numero_particulas)+'.csv', 'a')
    arquivo.write(texto + '\n')
    arquivo.close()


def conteudo_arquivo(global_best):

    texto = ''
    for p in global_best:
        texto = texto + ' ' + str(round(p.fit, 5)).replace('.', ',')
    return texto
