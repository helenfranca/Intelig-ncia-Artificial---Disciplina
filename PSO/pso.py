import Particula
import bib
import random


def pso():

    # Inicializando constantes
    c1 = 2.05
    c2 = 2.05
    w = 0.72

    grupo_iteracao = [20, 50, 100]
    grupo_populacao = [50, 100]

    for iteracoes in grupo_iteracao:
        for numero_particulas in grupo_populacao:

            numero_posicao_particula = 2
            vezes = 10
            loop = 0
            global_best_best = []
            while (loop < vezes):

                global_best = []

                # Criando as particulas
                enxame = bib.cria_particula(numero_particulas)

                # Inicializando a posição de cada particula
                bib.inicializa_posicao(enxame, numero_posicao_particula)

                # Inicializando a velocidade | deslocamento de cada particula
                # Nesse primeiro momento todas as particulas terão a mesma velocidade | deslocamento
                bib.inicializa_velocidade(enxame, numero_posicao_particula)

            #   -----------

                for i in range(0, iteracoes):
                    fit = 0
                    for particula in enxame:

                        # Calculando Fitness
                        fit = bib.fitness(particula.posicao)

                        # Calculando o pBest
                        bib.pBest(particula, fit)

                    # Descobrindo o gBest
                    ordenado = sorted(
                        enxame, key=Particula.Particula.get_fitness)
                    global_best.append(ordenado[0])

                    for particula in enxame:

                        for i in range(0, len(particula.velocidade)):
                            # Calcula a velocidade/deslocamento
                            particula.velocidade[i] = bib.velocidade(
                                w, particula, i, c1, c2, global_best)

                            # Calcula a posicão
                            bib.calcula_posicao(particula, i)

                global_best_best.append(global_best)

                texto = bib.conteudo_arquivo(global_best)

                bib.escreve_arquivo(texto, iteracoes, numero_particulas)

                loop = loop + 1


pso()
