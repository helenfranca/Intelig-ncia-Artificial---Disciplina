import random
import math

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
    
    def mutacao(self):
        bits = self.get_corpo()
        for i in range(0, len(bits)):
            taxa_mutacao = random.uniform(0, 1)

            if(taxa_mutacao <= 0.1):
                if(bits[i] == 0):
                    bits[i] = 1
                else:
                    bits[i] = 0

        self.corpo = bits


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
    pop = populacao.copy()
    for _ in range(0, len(pop)):
        a = random.choice(pop)  # Pega um cromossomo
        b = random.choice(pop)  # Pega um cromossomo

    
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
    while tam < len(pai):
        taxa_cross = random.uniform(0, 1) * 100

        paiUm = pai[tam]
        paiDois = pai[tam + 1]

        if taxa_cross <= 90:
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


def mediaMelhores(melhores, geracao):
    media = []
    
    for linha in melhores:
        somatorio = 0
        for item in linha:
            somatorio += item

        media.append(somatorio/geracao)

    return media


def conteudo_arquivo(melhores, geracao):
    texto = ''

    texto = '\t;Iter 1; Iter 2; Iter 3; Iter 4; Iter 5; Iter 6; Iter 7; Iter 8; Iter 9; Iter 10; \n Gen 1;'
    j = 1


    for cromossomo in melhores:
        j = j + 1
        for i in range(0, len(cromossomo)):
            # print(cromossomo)
            texto = texto + str(round(cromossomo[i], 5)).replace('.', ',') + ';'

        texto = texto + '\n Gen ' + str(j) + ';'


    texto += '\n\n'

    media = mediaMelhores(melhores, geracao)
    
    texto += 'Média Gen: ;'
    for valor in media:
        texto += str(round(valor, 5)) + ';'

    texto += '\n\n'   
  
    return texto

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

        escreve_arquivo(conteudo_arquivo(melhores_melhores, geracao), geracao)
        

main()
