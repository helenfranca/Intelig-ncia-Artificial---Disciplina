import random
import math

class Cromossomo:
    def __init__(self, valor):
        self.valor = valor
        self.x = (-20) + (20 + 20) * (self.valor / (pow(2, 10) - 1))
        self.aptidao = math.cos(self.x) * self.x + 2

    def get_valor(self):
        return self.valor

    def get_x(self):
        return self.x

    def get_aptidao(self):
        return self.aptidao

    def atualiza(self):

        self.x = (-20) + (20 + 20) * (self.valor / (pow(2, 10) - 1))
        self.aptidao = math.cos(self.x) * self.x + 2
        
    #mutacao de limite
    def mutacao(self):
        taxa_mutacao = random.uniform(0, 1)

        if(taxa_mutacao <= 0.1):
                
            if(random.uniform(0,1) < 0.5):
                self.valor = -20
            else:
                self.valor = 20

def cria_populacao(numero_populacao):

    populacao = [
        Cromossomo(random.uniform(-20, 20)) for x in range(0, numero_populacao)
    ]
    return populacao


def selecao_torneio(populacao):
    pais = []
    pop = populacao.copy()
    for _ in range(0, len(pop)):
        a = random.choice(pop)  # Pega um cromossomo
        b = random.choice(pop)  # Pega um cromossomo

    # Verifica quem é menor. O menor se torna um pai para a nova geração
        if (a.get_aptidao() < b.get_aptidao()):
            pai = a
        else:
            pai = b

        pais.append(pai)

    return pais


def crossover_mutacao(pais):
    nova_geracao = []
    tam = 0
    pai = pais.copy()

    alpha = 0.5
    
    while tam < len(pai):
        taxa_cross = random.uniform(0, 1) * 100

        paiUm = pai[tam]
        paiDois = pai[tam + 1]

        if taxa_cross <= 90:
            # Cruzamento

            beta = random.uniform((-1 * alpha), (1 + alpha))

            cromossomo_pai_um = paiUm.get_valor()
            cromossomo_pai_dois = paiDois.get_valor()

            filhoUm = cromossomo_pai_um + (beta * (cromossomo_pai_dois - cromossomo_pai_um))
            filhoDois = cromossomo_pai_dois + (beta * (cromossomo_pai_um - cromossomo_pai_dois))

            filhoUm = Cromossomo(filhoUm)
            filhoDois = Cromossomo(filhoDois)

        else:
            filhoUm = paiUm
            filhoDois = paiDois

        filhoUm.mutacao()
        filhoDois.mutacao()

        filhoUm.atualiza()
        filhoDois.atualiza()

        nova_geracao.append(filhoUm)
        nova_geracao.append(filhoDois)
        tam = tam + 2

    return nova_geracao


def elitismo(nova_geracao, populacao):

    melhor_pai = sorted(populacao, key=Cromossomo.get_aptidao)[0]
    filhos_ordenados = sorted(nova_geracao, key=Cromossomo.get_aptidao, reverse=True)
    pior_filho = filhos_ordenados[0]
    indice = nova_geracao.index(pior_filho)

    if melhor_pai.get_aptidao() < pior_filho.get_aptidao():
        nova_geracao[indice] = melhor_pai
    return nova_geracao


def escreve_arquivo(texto, geracao):
    arquivo = open('geracao_'+str(geracao)+'.csv', 'w')
    arquivo.write(texto + '\n')
    arquivo.close()


def conteudo_arquivo(melhores):
    texto = ''

    texto = '\t;Iter 1; Iter 2; Iter 3; Iter 4; Iter 5; Iter 6; Iter 7; Iter 8; Iter 9; Iter 10 \n Gen 1;'
    j = 1
    for cromossomo in melhores:
        j = j + 1
        for i in range(0, len(cromossomo)):
            # print(cromossomo)
            texto = texto + str(round(cromossomo[i], 5)).replace('.', ',') + ';'
        texto = texto + '\n Gen ' + str(j) + ';'

    texto += '\n\n'
  
    return texto


def imprimeEnxame(enxame):
    for particula in enxame:
        print(str(round(particula.get_aptidao(), 5)), end=" ")
    print()


def main():

    numero_populacao = 10
    pais = []
    geracoes = [10,20]
    
    for geracao in geracoes:
        melhores_melhores = []
        
        for _ in range(0,geracao):

            # 1° Passo: Criar População c/ aptidão
            populacao = cria_populacao(numero_populacao)
            melhores = []
            cruzado = []   
            for _ in range(0,numero_populacao):
                               
                # 2° Passo: Seleção por Torneio
                pais = selecao_torneio(populacao)
            
                # 3° Passo: Crossover & Mutação & Atualiza
                cruzado = crossover_mutacao(pais)      
            
                # 4° Passo: Elitismo
                new_geracao = elitismo(cruzado, populacao)

                populacao = new_geracao

                melhor_geracao = sorted(populacao, key=Cromossomo.get_aptidao)[0]
                melhor_geracao_aptidao = melhor_geracao.get_aptidao()
                melhores.append(melhor_geracao_aptidao)

            melhores_melhores.append(melhores)

        escreve_arquivo(conteudo_arquivo(melhores_melhores), geracao)

main()
