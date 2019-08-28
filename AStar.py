import time
import sys

class Node:

    def __init__(self, pai, posicao):
        self.g = 0
        self.h = 0
        self.f = 0
        self.posicao = posicao

        self.pai = pai

    def __eq__(self, other):
        if other is not Node:
            return self.posicao == other
        else:
            return self.posicao == other.posicao


# Heuristica baseada na função distância de Manhattan (calculo literal da distância do nó atual e o nó destino - desconsiderando barreiras)
def calcH(vizinhoPos,fimPos):
    return ((abs(vizinhoPos[0]-fimPos[0]))+(abs(vizinhoPos[1]-fimPos[1])))
    

# Função que define os vizinhos "possiveis" do nó atual (definido na função buscaMenorF)
def defVizinhos(matriz,atual,lstAberta,lstVizinhos,posPossiveis,tamLMatriz,tamCMatriz):
    
    for item in posPossiveis:
        
        posEncontrada = (atual.posicao[0]+item[0],atual.posicao[1]+item[1])
                
        if  ((posEncontrada[0]<tamLMatriz and posEncontrada[0]>=0) and (posEncontrada[1]<tamCMatriz and posEncontrada[1]>=0)):
            if(matriz[posEncontrada[0]][posEncontrada[1]] != 1):
                lstVizinhos.append(Node(atual, posEncontrada))
    return lstVizinhos


        
# Função que busca o menor caminhoo (g+h) até o destino    
def buscaMenorF(lstAberta):
    menorF = lstAberta[0]

    for i in range(1, len(lstAberta)):
        if (menorF.f > lstAberta[i].f):
            menorF = lstAberta[i]

    return menorF
    
    
# Função que faz o caminho baseado nos "pais" dos nós
def caminho(atual, inicio):
    caminho = [atual.posicao]

    while atual.posicao != inicio.posicao:
        caminho.append(atual.pai.posicao)
        atual = atual.pai
    return caminho


# Função que adiciona caractere no indíce que faz parte do caminho para o destino
def desenhaCaminho(matriz, caminho):
    for item in caminho:
        matriz[item[0]][item[1]] = '*'
    return matriz


# Função que printa a matriz
def printaMatriz(matriz):
    print()
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(" ",matriz[i][j], end= "")
        print()
        

# Função que lê a matriz do arquivo
def leMatriz(matriz_arq):
    matriz = []
    
    with open(matriz_arq, 'r') as f:
        l = [[int(num) for num in line.split(' ') if num != '\n'] for line in f]
    
    return l
   

    
lstAberta = []
lstFechada = []
atualPos = tuple([int(x) for x in sys.argv[2].split(',')])
fimPos = tuple([int(x) for x in sys.argv[3].split(',')])


matriz = leMatriz(sys.argv[1])


lstVizinhos = []
posPossiveis = ((-1,0), (1,0), (0,-1), (0, 1))
tamLMatriz = len(matriz)
tamCMatriz = len(matriz[0])



inicio = Node(None, atualPos)
fim = Node(None, fimPos)
    

if (matriz[atualPos[0]][atualPos[1]] == 1):
	print("ERRO! Posição inicial é um obstáculo.") 
	sys.exit(0)
	
if (matriz[fimPos[0]][fimPos[1]] == 1):
	print("ERRO! Posição final é um obstáculo.")
	sys.exit(0)

if (fimPos == atualPos):
	print("Posição destino == Posição fim")
	sys.exit(0)


lstAberta.append(inicio)

while(len(lstAberta) > 0):
	
    #definição do nó atual como sendo o que possui menor distância até o destino    
    atual = buscaMenorF(lstAberta)

	#se a posicao do nó atual for igual a posicao do nó destino significa que chegamos ao nó destino
    if (atual.posicao == fim.posicao): break
        
    
    #adiciona o no atual na lista fechada e remove da lista aberta...afinal ele ja foi analisado
    lstAberta.remove(atual)
    lstFechada.append(atual)


	#definimos os vizinhos "possiveis" do no atual
    vizinhos = defVizinhos(matriz,atual,lstAberta,lstVizinhos,posPossiveis,tamLMatriz,tamCMatriz)
        
    #para cada vizinho possivel 
    for vizinho in vizinhos:
		
		#verificamos se esta na lista fechada, se estiver, passa para o proximo vizinho
        if (vizinho in lstFechada): continue

		#se ele nao esta na lstAberta qr dizer que ainda nao sabemos os valores do F, portanto calculamos e o adicionamos na lstAberta
        if (vizinho not in lstAberta):
            vizinho.pai = atual
            vizinho.g = atual.g + 1
            vizinho.h = calcH(vizinho.posicao,fimPos)
            vizinho.f = vizinho.g + vizinho.h
            lstAberta.append(vizinho)

		#se o vizinho esta na lstAberta e "passando pelo nó atual o valor de g do vizinho é menor do que o que ele tem agora?" entao recalculamos os valores de g,h e f
		#e mudamos o pai dele para o nó atual
        elif (vizinho in lstAberta and ((atual.g+1) < vizinho.g)):
            vizinho.g = atual.g+1
            vizinho.h = calcH(vizinho.posicao,fimPos)
            vizinho.f = vizinho.g + vizinho.h
            vizinho.pai = atual

caminho = caminho(atual, inicio)

caminho.reverse()

print(caminho)

printaMatriz(desenhaCaminho(matriz,caminho)) 
