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


def conteudo_arquivo(melhores, geracao, media):
    texto = ''

    if (geracao == 10):

        texto = '\t;Gen 1; Gen 2; Gen 3; Gen 4; Gen 5; Gen 6; Gen 7;  Gen 8; Gen 9; Gen 10 \n Exe 1;'

    else:

        texto = '\t;Gen 1; Gen 2; Gen 3; Gen 4; Gen 5; Gen 6; Gen 7;  Gen 8; Gen 9; Gen 10; Gen 11; Gen 12; Gen 13; Gen 14; Gen 15; Gen 16; Gen 17;  Gen 18; Gen 19; Gen 20\n Exe 1;'
        
    j = 1
    for cromossomo in melhores:
        j = j + 1
        for i in range(0, len(cromossomo)):
            # print(cromossomo)
            texto = texto + str(round(cromossomo[i], 5)).replace('.', ',') + ';'
        texto = texto + '\n Exe ' + str(j) + ';'

    texto += '\n\n'

    texto += 'Média: ;'

    for valor in media:
        texto = texto + str(round(valor, 5)).replace('.', ',') + ';'

 
    return texto

def media_melhores(melhores):
    media_melhores = []
   
    for linha in melhores:
        soma = 0
        for cromossomo in linha:
            soma += cromossomo
        media_melhores.append(soma/10)

    return media_melhores


def grafico(geracao, media, melhor_solucao):
    import matplotlib.pyplot as plt

    x = [i for i in range(1, geracao+1)]

    plt.plot(x, media, label="Média")
    plt.plot(x, melhor_solucao, label="Melhor solução")
    plt.title("Representação Binária")
    plt.ylabel("Aptidão")
    plt.xlabel("Gerações")
    plt.grid()
    plt.legend(loc="best")
    plt.savefig('geracao' +str(geracao)+ '.png')
    plt.close()

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
        
        for _ in range(10):

            # 1° Passo: Criar População c/ aptidão
            populacao = cria_populacao(numero_populacao)
            melhores = []
            cruzado = []
            
            for _ in range(geracao):
                               
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

        for i in range(len(melhores_melhores)):
            print(melhores_melhores[i])
           
       
        media = []
        for i in range(geracao): #Quantidade de GERACOES
            media.append(0)
            for j in range(10): #Quantidade de EXECUCOES
                media[i] += melhores_melhores[j][i]
            media[i] /= 10

        print("media: ", media)


        pos_melhor = 0
        menor_aptidao = melhores_melhores[0][-1]
        
        for i in range(1, len(melhores_melhores)):
            if (menor_aptidao > melhores_melhores[i][-1]):
                menor_aptidao = melhores_melhores[i][-1]
                pos_melhor = i

        melhor_solucao = melhores_melhores[pos_melhor]


        ##print(pos_melhor, '\n\n')

        ##print(melhor_solucao)

        grafico(geracao, media, melhor_solucao)


        escreve_arquivo(conteudo_arquivo(melhores_melhores, geracao, media), geracao)


main()
