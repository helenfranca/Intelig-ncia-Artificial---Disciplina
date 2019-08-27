import time

class Node():
    """A node class for A* caminhofinding"""

    def __init__(self, pai=None, posicao=None):
        self.pai = pai
        self.posicao = posicao

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, outro):
        return self.posicao == outro.posicao


def aestrela(mapa, start, end):
    """Retorna a lista de tuplas com o caminho, do início ao fim"""


    # Cria o nó de início e o nó de fim
    no_inicio = Node(None, start)
    no_inicio.g = no_inicio.h = no_inicio.f = 0
    no_fim = Node(None, end)
    no_fim.g = no_fim.h = no_fim.f = 0

    # Inicializa a lista aberta e a lista fechada
    lista_aberta = []
    lista_fechada = []

    # Adiciona o nó inicial na lista aberta
    lista_aberta.append(no_inicio)

    # Loop até encontrar o nó final
    while len(lista_aberta) > 0:

        # Pega o nó corrente
        no_corrente = lista_aberta[0]
        index_corrente = 0
        for index, item in enumerate(lista_aberta):
            if item.f < no_corrente.f:
                no_corrente = item
                index_corrente = index

        # Retira o nó da lista aberta e adiciona na lista fechada
        lista_aberta.pop(index_corrente)
        lista_fechada.append(no_corrente)

        # Encontrou o final == objetivo
        if no_corrente == no_fim:
            caminho = []
            corrente = no_corrente
            while corrente is not None:
                caminho.append(corrente.posicao)
                corrente = corrente.pai
            return caminho[::-1] # Retorna o caminho

        # Gera a lista de nós filhos
        filhos = []
        for nova_posicao in [(-1,0), (1,0), (0,-1), (0, 1)]: # quadrados adjacentes
            # Pega a posição do nó
            posicao_no = (no_corrente.posicao[0] + nova_posicao[0], no_corrente.posicao[1] + nova_posicao[1])

            # Verifica se está dentro do mapa
            if posicao_no[0] > (len(mapa) - 1) or posicao_no[0] < 0 or posicao_no[1] > (len(mapa[len(mapa)-1]) -1) or posicao_no[1] < 0:
                continue

            # Verifica se está acessível
            if mapa[posicao_no[0]][posicao_no[1]] != 0:
                continue

            # Cria novo nó
            novo_no = Node(no_corrente, posicao_no)

            # Insere o novo nó na lista de filhos
            filhos.append(novo_no)

        for filho in filhos:
            # Para cada filho na lista fechada 
            for filho_fechada in lista_fechada:
                if filho == filho_fechada:
                    continue

            # Cálculo de F, G e H
            filho.g = no_corrente.g + 1
            filho.h = ((filho.posicao[0] - no_fim.posicao[0]) ** 2) + ((filho.posicao[1] - no_fim.posicao[1]) ** 2)
            filho.f = filho.g + filho.h

            # Para cada filho na lista aberta
            for no in lista_aberta:
                if filho == no and filho.g > no.g:
                    continue

            # Adiciona o no_filho na lista aberta
            lista_aberta.append(filho)


def main():

    mapa2 = [[0, 0, 1, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 0],
            [1, 0, 0, 1]]

    mapa0 = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    manipulador = open('mapa.txt','r')
    mapa = []
    for linha in manipulador:
        b = []
        for elem in linha:
            if elem != ' ' and elem != '\n':
                b.append(int(elem))
        mapa.append(b)
    manipulador.close()
    print(mapa)

    """ Falta mudar as variaveis de objetivo, inicio e testar os mapas. Inserir elementos por linha de comando"""

    inicio = (0, 0)
    fim = (2,3)
    tempo_inicial = time.time()
    caminho = aestrela(mapa, inicio, fim)

    print(caminho)
    print("\n--- %s segundos ---" % (time.time() - tempo_inicial))


if __name__ == '__main__':
    main()