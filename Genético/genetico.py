import random
import math
import numpy as np

import matplotlib
import matplotlib.pyplot as plt


class Cromossomo:
    def __init__(self, corpo):
        self.corpo = corpo

        # Normaliza
        dec = bin2Dec(formata(self.corpo))
        self.x = (-20) + (20 + 20) * (dec / (pow(2, 10) - 1))

        # Calcula a aptidao baseado no numero normalizado
        self.aptidao = math.cos(self.x) * self.x + 2

    def get_corpo(self):
        return self.corpo

    def get_x(self):
        return self.x

    def get_aptidao(self):
        return self.aptidao

    def atualiza(self):
        dec = bin2Dec(formata(self.corpo))
        self.x = (-20) + (20 + 20) * (dec / (pow(2, 10) - 1))
        self.aptidao = math.cos(self.x) * self.x + 2


def cria_cromossomo():

    cromossomo = [random.randrange(0, 2) for x in range(0, 10)]

    return cromossomo


def cria_populacao(numero_populacao):

    populacao = [
        Cromossomo(cria_cromossomo()) for x in range(0, numero_populacao)
    ]
    return populacao


def selecao_torneio(populacao):
    pais = []

    for _ in range(0, len(populacao)):
        a = random.choice(populacao)  # Pega um cromossomo
        b = random.choice(populacao)  # Pega um cromossomo

    # Verifica quem é menor. O menor se torna um pai para a nova geração
        if (a.get_aptidao() < b.get_aptidao()):
            pai = a
        else:
            pai = b

        pais.append(pai)

    return pais


def crossover(pais):
    nova_geracao = []
    tam = 0
    while tam < len(pais):
        taxa_cross = random.uniform(0, 1) * 100

        paiUm = pais[tam]
        paiDois = pais[tam + 1]

        if taxa_cross <= 60:
            # Cruzamento
            corte = random.randrange(1, 10)
            cromossomo_pai_um = paiUm.get_corpo()
            cromossomo_pai_dois = paiDois.get_corpo()

            filhoUm = cromossomo_pai_um[0:corte] + cromossomo_pai_dois[corte:]
            filhoDois = cromossomo_pai_dois[0:corte] + \
                cromossomo_pai_um[corte:]

            filhoUm = Cromossomo(filhoUm)
            filhoDois = Cromossomo(filhoDois)

        else:
            filhoUm = paiUm
            filhoDois = paiDois

        nova_geracao.append(filhoUm)
        nova_geracao.append(filhoDois)
        tam = tam + 2

    return nova_geracao


def mutacao(nova_geracao):
    for filho in nova_geracao:
        cromossomo = filho.get_corpo()

        for i in range(0, len(cromossomo)):
            taxa_mutacao = random.randrange(0, 2)
            if(taxa_mutacao == 1):
                if(cromossomo[i] == 0):
                    cromossomo[i] = 1
                else:
                    cromossomo[i] = 0
        filho.atualiza()
    return nova_geracao


def elitismo(nova_geracao, populacao):
    print('\nELITISMO: ----------')

    melhor_pai = sorted(populacao, key=Cromossomo.get_aptidao)[0]
    filhos_ordenados = sorted(
        nova_geracao, key=Cromossomo.get_aptidao, reverse=True)
    pior_filho = filhos_ordenados[0]
    indice = nova_geracao.index(pior_filho)

    print("Melhor pai: ", melhor_pai.get_aptidao(),
          '\nPior filho:', pior_filho.get_aptidao(), '\n')

    # print('PAIS --->', end=" ")
    # for particula in populacao:
    #     print(str(round(particula.get_aptidao(), 5)), end=" ")
    # print()

    # print('FILHOS --->', end=" ")
    # for particula in nova_geracao:
    #     print(str(round(particula.get_aptidao(), 5)), end=" ")
    # print()

    if melhor_pai.get_aptidao() < pior_filho.get_aptidao():
        nova_geracao[indice] = melhor_pai
    return nova_geracao


def escreve_arquivo(texto, geracao):
    arquivo = open('geracao_'+str(geracao)+'.csv', 'w')
    arquivo.write(texto + '\n')
    arquivo.close()


def conteudo_arquivo(melhores):
    texto = ''

    texto = '\t;Gen 1; Gen 2; Gen 3;Gen 4; Gen 5; Gen 6;Gen 7; Gen 8; Gen 9; Gen 10 \n Iteracao 1;'
    j = 1
    for cromossomo in melhores:
        j = j + 1
        for i in range(0, len(cromossomo)):
            # print(cromossomo)
            texto = texto + \
                str(round(cromossomo[i], 5)).replace('.', ',') + ';'
        texto = texto + '\n Iteracao ' + str(j) + ';'

    texto += '\n\n'
    '''
    texto += 'Média: ;'
    for item in media_melhores:
        
        texto += str(round(item, 5)).replace('.', ',') + ';'
    '''
    return texto


def calcula_media(melhores, geracao):
    media_melhores = []

    for linha in melhores:
        somatorio = 0
        for item in linha:
            somatorio += item
        media_melhores.append(somatorio/geracao)
    return media_melhores


def bin2Dec(binary):

    decimal, i = 0, 0
    while (binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return decimal


def formata(corpo):
    b = ''
    for i in corpo:
        b = str(i) + '' + b
    return int(b)


def imprimeEnxame(enxame):
    for particula in enxame:
        print(str(round(particula.get_aptidao(), 5)), end=" ")
    print()


def defineMelhor(ultimaLinha):

    menor = ultimaLinha[0]
    j = 0
    for i in range(1, len(ultimaLinha)-1):
        if menor > ultimaLinha[i]:
            menor = ultimaLinha[i]
            j = i  # guarda posicao do menor
    return menor, j


def listaMelhorGen(melhores, indice):
    melhorGen = []
    for linha in melhores:
        melhorGen.append(linha[indice])
    return melhorGen


def main():

    numero_populacao = 10
    pais = []
    nova_geracao = []

    geracoes = [10]
    melhores_melhores = []

    # 1° Passo: Criar População c/ aptidão
    populacao = cria_populacao(numero_populacao)
    '''
    for geracao in geracoes:
        melhores_melhores = []
    for _ in range(0,10):
    '''
    melhores = []
    for _ in range(0, 10):
        print("\n /==============================================================/ \n")
        # 2° Passo: Seleção por Torneio
        populacao = selecao_torneio(populacao)

        # 3° Passo: Crossover
        nova_geracao = crossover(populacao)

        # 4° Passo: Mutação
        nova_geracao = mutacao(nova_geracao)

        imprimeEnxame(populacao)
        imprimeEnxame(nova_geracao)

        # 5° Passo: Elitismo
        nova_geracao = elitismo(nova_geracao, populacao)

        populacao = nova_geracao

        # populacao = selecao_torneio(nova_geracao)

        imprimeEnxame(nova_geracao)

        melhor_geracao = sorted(nova_geracao, key=Cromossomo.get_aptidao)[0]
        melhor_geracao_aptidao = melhor_geracao.get_aptidao()
        melhores.append(melhor_geracao_aptidao)

    melhores_melhores.append(melhores)

    transposta = np.transpose(melhores_melhores)
    #  print(transposta, '\n')
    escreve_arquivo(conteudo_arquivo(transposta), 10)

    # -------------------------------------
'''
        print()
        print("geracao" + str(geracao)+ " :",transposta)
        print() 

        media = calcula_media(transposta, geracao)

        print()

        # mando ultima linha da matriz de resultado para definicao do menor
        melhor_Gen = defineMelhor(transposta[-1])

        # print("melhor_Gen: ", melhor_Gen)

        # print("media: ", media)

        print()
        
        # lista melhor Gen a partir do ultimo melhor
        lstMelhorGen = listaMelhorGen(transposta, melhor_Gen[1])

        # print("lst melhor Gen: ", lstMelhorGen)


        

        escreve_arquivo(conteudo_arquivo(transposta, media), geracao)

        geracao_x_grafico = [x for x in range(1, geracao+1)]
        
        # grafico
        fig, ax = plt.subplots()
        color = 'tab:red'
        plt.plot(geracao_x_grafico, media, color=color, label='Média')
        color = 'tab:blue'
        plt.xlabel('Geração')
        plt.ylabel('Aptidão')
        plt.plot(geracao_x_grafico, lstMelhorGen, color=color, label='Melhor Gen')
        plt.grid(True)
        plt.legend(loc=0)
        plt.savefig('graficoGeracao_'+str(geracao)+'.png')

'''


main()
