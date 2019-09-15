import random
import math

class Particula:
    def __init__(self,posicao,velocidade,fit,pBest):
        self.posicao = posicao
        self.velocidade = velocidade
        self.fit = fit
        self.pBest = pBest
    

def fitness(posicao):
    return (- (posicao[1] + 47) * math.sin(math.sqrt(math.fabs((posicao[0] / 2) + (posicao[1] + 47))))) - (posicao[0] * math.sin(math.sqrt(math.fabs(posicao[0] - (posicao[1] + 47)))))
    
# Revisar a lógica do GBest
def gBest(enxame):
    menor = []
    gbest = [512,512]
    pos = 0
    for particula in enxame:
        menor.append(particula.pBest.posicao)
    
    for posicao in menor:
        if posicao[0] < gbest[0] and posicao[1] < gbest[1]:
            gbest[0] = posicao[0]
            gbest[1] = posicao[1]
            pos = posicao
    
    return pos


def cria_particula(numero_particulas):
    return enxame = [ Particula(0,1,2,3) for x in range(0, numero_particulas)]


def inicializa_posicao(enxame,numero_posicao_particula):
    for particula in enxame:
        
        posicao_particula = [random.uniform(-512,512) for j in range(0,numero_posicao_particula)]
        particula.posicao = posicao_particula

def inicializa_velocidade(enxame, numero_posicao_particula):
     for particula in enxame:
        
        velocidade_particula = [1 for j in range(0,numero_posicao_particula)]
        particula.velocidade = velocidade_particula


def main():

    # Inicializando constantes
    c1 = 1
    c2 = 1
    w = 0.72

    global_best = []

    # Tornar parametrizado
    numero_particulas = 20
    numero_posicao_particula = 2
    

    # Criando as particulas
    enxame = cria_particula(numero_particulas)
    

    # Inicializando a posição de cada particula
    inicializa_posicao(enxame,numero_posicao_particula)
    

    # Inicializando a velocidade | deslocamento de cada particula
    # Nesse primeiro momento todas as particulas terão a mesma velocidade | deslocamento
    inicializa_velocidade(enxame, numero_posicao_particula)
    #   -----------


    for particula in enxame:

        # Calculando Fitness
        particula.fit = fitness(particula.posicao)

        # PBest | No momento o melhor é a posição atual porque é a primeira. 
        # Não houve outra pra que pudesse ser comparada
        particula.pBest = particula

    # Descobrindo o gBest
    # print(global_best.append(gBest(enxame)))
    print(particula(enxame[0].posicao))




    # print(enxame[0].pBest.posicao, enxame[0].posicao )



main()