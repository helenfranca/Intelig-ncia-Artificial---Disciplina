import time
class Node:

    def __init__(self, pai, posicao):
        self.g = 0
        self.h = 0
        self.f = 0
        self.posicao = posicao

        self.pai = pai



def calcH(vizinhoPos,fimPos):
    return ((abs(vizinhoPos[0]-fimPos[0]))+(abs(vizinhoPos[1]-fimPos[1])))
    

def defVizinhos(matriz,atual,lstAberta,lstVizinhos,posPossiveis,tamLMatriz,tamCMatriz):
    '''lstVizinhos = []
    posPossiveis = ((-1,0), (1,0), (0,-1), (0, 1))
    tamLMatriz = len(matriz)
    tamCMatriz = len(matriz[0])'''
    
    for item in posPossiveis:
        
        posEncontrada = (atual.posicao[0]+item[0],atual.posicao[1]+item[1])
                
        if  ((posEncontrada[0]<tamLMatriz and posEncontrada[0]>=0) and (posEncontrada[1]<tamCMatriz and posEncontrada[1]>=0)):
            if(matriz[posEncontrada[0]][posEncontrada[1]] != 1):
                lstVizinhos.append(Node(atual, posEncontrada))
                '''if len(lstAberta)>0:
                    for item in lstAberta:
                        if item.posicao != posEncontrada:
                            lstVizinhos.append(Node(atual, posEncontrada))
                else:
                    lstVizinhos.append(Node(atual, posEncontrada))'''
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

tempo_inicial = time.time()
    
    
matriz = [[0, 0, 1, 0, 0, 0],
          [0, 0, 1, 0, 0, 0],
          [0, 0, 1, 0, 0, 0],
          [0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 1, 0]]
    
    
lstVizinhos = []
posPossiveis = ((-1,0), (1,0), (0,-1), (0, 1))
tamLMatriz = len(matriz)
tamCMatriz = len(matriz[0])

lstAberta = []
lstFechada = []
atualPos = (0,0)
fimPos = (4,5)

inicio = Node(None, atualPos)
fim = Node(None, fimPos)
    

matriz1 = [[0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 1, 0, 0, 1, 1, 1],
             [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]]
             

atual = inicio

lstAberta.append(inicio)

while(atual.posicao != fimPos or len(lstAberta) != 0):
        
    atual = buscaMenorF(lstAberta)

    if (atual.posicao == fim.posicao): break
        
    lstAberta.remove(atual)
    lstFechada.append(atual)

    vizinhos = defVizinhos(matriz,atual,lstAberta,lstVizinhos,posPossiveis,tamLMatriz,tamCMatriz)
        
    for vizinho in vizinhos:
        if (vizinho in lstFechada): continue

        if (vizinho not in lstAberta):
            vizinho.pai = atual
            vizinho.g = atual.g + 1
            vizinho.h = calcH(vizinho.posicao,fimPos)
            vizinho.f = vizinho.g + vizinho.h
            lstAberta.append(vizinho)

        elif (vizinho in lstAberta and ((atual.g+1) < vizinho.g)):
            vizinho.g = atual.g+1
            vizinho.h = calcH(vizinho.posicao,fimPos)
            vizinho.f = vizinho.g + vizinho.h
            vizinho.pai = atual

caminho = caminho(atual, inicio)

print(caminho)
print("\n--- %s segundos ---" % (time.time() - tempo_inicial))
