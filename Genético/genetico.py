import random
import math


class Cromossomo:
    def __init__(self,corpo):
        self.corpo = corpo
        num = bin2Dec(formata(corpo))
        self.aptidao = math.cos(num) * num + 2

    def get_corpo(self):
        return self.corpo

    def get_aptidao(self):
        return self.aptidao

def cria_cromossomo():

    cromossomo = [random.randrange(0,2) for x in range(0, 10)]

    return cromossomo

def cria_populacao(numero_populacao):

    populacao = [Cromossomo(cria_cromossomo()) for x in range(0, numero_populacao)]
    return populacao

def bin2Dec(binary): 
      
    decimal, i = 0, 0
    while(binary != 0): 
        dec = binary % 10
        decimal = decimal + dec * pow(2, i) 
        binary = binary//10
        i += 1
    return decimal

def formata(a):
    b = ''
    for i in a:
        b = str(i) + '' +b
    return int(b) 

def main():
    numero_populacao = 5
    
    # 1° Passo: Criar População e calcular aptidão
    populacao = cria_populacao(numero_populacao)
    # print(populacao[0].get_corpo(), populacao[0].aptidao)
    

    # 2° Passo: Seleção por Torneio
    # print(bin2Dec(formata([1,0,1,0,1])))
   



main()