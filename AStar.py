class Node:

    def __init__(self, pai, posicao):
        self.g = 0
        self.h = 0
        self.f = 0
        self.posicao = posicao

        self.pai = pai



def calcH(atualPos,fimPos):
    return ((abs(atualPos[0]-fimPos[0]))+(abs(atualPos[1]-fimPos[1])))
    

def defVizinhos(matriz, atual):
    lstVizinhos = []
    posPossiveis = ((-1,0), (1,0), (0,-1), (0, 1))
    tamLMatriz = len(matriz)
    tamCMatriz = len(matriz[0])
    
    for item in posPossiveis:
        posEncontrada = (atual.posicao[0]+item[0],atual.posicao[1]+item[1])
                
        if  ((posEncontrada[0]<tamLMatriz and posEncontrada[0]>=0) and
        (posEncontrada[1]<tamCMatriz and posEncontrada[1]>=0)):
            if(matriz[posEncontrada[0]][posEncontrada[1]] != 1):
                lstVizinhos.append(Node(atual, posEncontrada))
    return lstVizinhos


        
    
def buscaMenorF(lstAberta):
    menorF = lstAberta[0]

    for i in range(1, len(lstAberta)):
        if (menorF.f > lstAberta[i].f):
            menorF = lstAberta[i]

    return menorF

def caminho(atual, inicio):
    caminho = [atual.posicao]

    while atual.posicao != inicio.posicao:
        caminho.append(atual.pai.posicao)
        atual = atual.pai
    return caminho
        

lstAberta = []
lstFechada = []
atualPos = (0,0)
fimPos = (9,8)

inicio = Node(None, atualPos)
fim = Node(None, fimPos)
    

matriz = [[0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 1, 0, 0, 1, 1, 1],
             [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]]


lstAberta.append(inicio)

while(len(lstAberta) != 0):
        
    atual = buscaMenorF(lstAberta)

    if (atual.posicao == fim.posicao): break
        
    lstAberta.remove(atual)
    lstFechada.append(atual)

    vizinhos = defVizinhos(matriz,atual)
        
    for vizinho in vizinhos:
        if (vizinho in lstFechada): break

        if (vizinho not in lstAberta):
            vizinho.pai = atual
            vizinho.g = atual.g + 1
            vizinho.h = calcH(atual.posicao,vizinho.posicao)
            vizinho.f = vizinho.g + vizinho.h
            lstAberta.append(vizinho)

        elif (vizinho in lstAberta and ((atual.g+1) < vizinho.g)):
            vizinho.g = atual.g+1
            vizinho.f = vizinho.g + vizinho.h
            vizinho.pai = atual

caminho = caminho(atual, inicio)

print(caminho)



