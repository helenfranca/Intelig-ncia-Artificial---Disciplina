## Atividade desenvolvida para a disciplina de Inteligência Artificial

### Membros
[Helen França](https://github.com/helenfranca)
<br>[Júlia Miranda](https://github.com/juliamrc)

### O Algoritmo PSO

O algoritmo de otimização por enxame de partículas é um tipo de inteligência de enxame inspirado no comportamento de bandos de pássaros. 
Sua modelagem é feita pelos pássaros (partículas) que fazem uso de sua experiência e da experiência do próprio bando para encontrar a 
melhor região do espaço de busca.

James Kennedy e Russel Eberhart, inspirados no comportamento social dos pássaros estudados pelo biológo Frank Heppner, desenvolveram uma 
técnica de otimização que veio a ser conhecida como enxame de partículas. Essa denominação se deu, pois se notou que o modelo escrito por 
Heppner demonstrava características de um enxame inteligente, onde seus membros que apresentavam tal comportamento foram generalizados 
para o termo partículas.

Para que o bando de pássaros sempre se aproxime do objetivo, utiliza-se o indicador denominado **fitness**, função que irá avaliar o 
desempenho das partículas. A partir disso, verificaríamos quem seria o ‘líder do bando’ (vamos chamar de **gbest**), ou seja, aquele indi-
víduo que tem a melhor rota dentre todos. Sabendo o líder, começamos a ‘cruzar’ (o termo em inglês correto é de ***crossover***) parte da 
sua rota com a dos outros indivíduos. Fazendo assim, na teoria, com que todos melhorem sua rota através do líder (melhor indivíduo).

Há também um segundo ‘crossover’ para cada indivíduo. Porém, nesse, nós misturamos a rota atual de cada indivíduo com a melhor rota já obtida pelo mesmo, anteriormente (chamamos de **pbest**).

#### A cada iteração...
1. Escolhemos o líder, dentre os indivíduos. (O que tem melhor resultado).
2. Fazemos um ***crossover*** de cada indivíduo com seu **pbest**.
3. Com a rota resultante fazemos um outro crossover, mas com o **gbest**.

### Problema proposto

Minimizar a função descrita pela equação abaixo, chamada Eggholder function, que é uma função clássica na condução de testes para otimização de funções:

![Eggholder function](https://github.com/helenfranca/Inteligencia_Artificial_Disciplina/blob/master/PSO/img/eggholder_fuction.png)

O objetivo é encontrar o mínimo global, descrito em:

![Mínimo Global](https://github.com/helenfranca/Inteligencia_Artificial_Disciplina/blob/master/PSO/img/minimo_global.png)

### Implementação

Divisão do código em três principais arquivos.

- **pso.py**: arquivo principal, a main() do projeto.
- **bib.py**: arquivo onde estão todas as funções utilizadas durante a execução.
- **Particula.py**: arquivo específico para descrição da classe da partícula.

#### Classe Partícula

```python
  class Particula:
    def __init__(self, posicao, velocidade, fit, pBest):
        self.posicao = posicao
        self.velocidade = velocidade
        self.fit = fit
        self.pBest = pBest

    def get_fitness(self):
        return self.fit
```

#### Calculo da aptidão (Fitness)

```python
def fitness(posicao):
    return (- (posicao[1] + 47) * math.sin(math.sqrt(math.fabs((posicao[0] / 2) + (posicao[1] + 47))))) - 
           (posicao[0] * math.sin(math.sqrt(math.fabs(posicao[0] - (posicao[1] + 47)))))
```

#### Atualiza velocidade da Partícula

```python
def velocidade(w, particula, i, c1, c2, global_best):
    veloz = (w * particula.velocidade[i]) + (c1 * random.uniform(0, 1) * (particula.pBest.posicao[i] - 
            particula.posicao[i])) + (c2 * random.uniform(0, 1) * (global_best[len(global_best)-1].posicao[i] 
            - particula.posicao[i]))

    if (veloz > 77):
        veloz = 77
    if (veloz < -77):
        veloz = -77

    return veloz
```

#### Atualiza posição da Partícula

```python
def calcula_posicao(particula, i):
    nova_posicao = 0
    nova_posicao = particula.posicao[i] + \
        particula.velocidade[i]

    if(nova_posicao > 512):
        particula.posicao[i] = 512
        particula.velocidade[i] = 0.0
    elif(nova_posicao < -512):
        particula.posicao[i] = -512
        particula.velocidade[i] = 0.0
    else:
        particula.posicao[i] = nova_posicao
```

#### Definindo o pBest

```python
def pBest(particula, fitness):

    if (particula.pBest == 3):
        particula.fit = fitness
        particula.pBest = particula
    elif (particula.fit > fitness):
        particula.fit = fitness
        particula.pBest = particula
```

#### Auxílio na escrita no arquivo

```python
def escreve_arquivo(texto, iteracoes, numero_particulas):
    arquivo = open(str(iteracoes)+'_' + str(numero_particulas)+'.csv', 'a')
    arquivo.write(texto + '\n')
    arquivo.close()


def conteudo_arquivo(global_best):
    texto = ''
    for p in global_best:
        texto = texto + ' ' + str(round(p.fit, 5)).replace('.', ',')
    return texto
```

#### PSO

```python
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
            
            while (loop < vezes):
                global_best = []
                
                # Criando as particulas
                enxame = bib.cria_particula(numero_particulas)

                # Inicializando a posição de cada particula
                bib.inicializa_posicao(enxame, numero_posicao_particula)

                # Inicializando a velocidade | deslocamento de cada particula
                # Nesse primeiro momento todas as particulas terão a mesma velocidade | deslocamento
                bib.inicializa_velocidade(enxame, numero_posicao_particula)

                for i in range(0, iteracoes):
                    fit = 0
                    
                    for particula in enxame:
                        # Calculando Fitness
                        fit = bib.fitness(particula.posicao)
                        # Calculando o pBest
                        bib.pBest(particula, fit)

                    # Descobrindo o gBest
                    ordenado = sorted(enxame, key=Particula.Particula.get_fitness)
                    global_best.append(ordenado[0])

                    for particula in enxame:
                        for i in range(0, len(particula.velocidade)):
                            # Calcula a velocidade/deslocamento
                            particula.velocidade[i] = bib.velocidade(w, particula, i, c1, c2, global_best)
                            # Calcula a posicão
                            bib.calcula_posicao(particula, i)

                texto = bib.conteudo_arquivo(global_best)
                bib.escreve_arquivo(texto, iteracoes, numero_particulas)
                loop = loop + 1
```

#### Resultados

Podemos perceber que ao início da execução (para x partículas com y iterações) as partículas possuem comportamento desordenado e aleatório. A partir do conhecimento e influência do gBest em cada partícula em uma iteração, elas passam a ter comportamento parecido, o que mostra que o código é eficaz e pouco aleatório.

Os gráficos abaixo são gerados por um editor de planilhas. Dado que após execução, o algoritmo escreve em arquivo CSV os gBests, o melhor e a média.

![Gráfico](https://github.com/helenfranca/Inteligencia_Artificial_Disciplina/blob/master/PSO/img/20_50.png)

![Gráfico](https://github.com/helenfranca/Inteligencia_Artificial_Disciplina/blob/master/PSO/img/20_100.png)

![Gráfico](https://github.com/helenfranca/Inteligencia_Artificial_Disciplina/blob/master/PSO/img/50_50.png)

![Gráfico](https://github.com/helenfranca/Inteligencia_Artificial_Disciplina/blob/master/PSO/img/50_100.png)

![Gráfico](https://github.com/helenfranca/Inteligencia_Artificial_Disciplina/blob/master/PSO/img/100_50.png)

![Gráfico](https://github.com/helenfranca/Inteligencia_Artificial_Disciplina/blob/master/PSO/img/100_100.png)

![Tabela](https://github.com/helenfranca/Inteligencia_Artificial_Disciplina/blob/master/PSO/img/tabela20_50.PNG)




### Rodando o algoritmo

##### Importante

É necessário ter Python3 instalado em sua máquina. Caso não tenha, [clique aqui](https://www.python.org/downloads/) e efetue os procedimentos.

- Faça um clone do projeto em sua IDE de preferência ou o download dos arquivos
- Por meio da linha de comando navegue até o diretório onde se encontram os arquivos-fonte

##### Via linha de comando, escreva:

- python pso.py


##### Lembre-se:

- Caso não possua os arquivos CSV na pasta em questão, o algoritmo irá criá-lo.

---







#### Referências
- [Introdução à Inteligência de Enxame](http://aimotion.blogspot.com/2009/04/introducao-inteligencia-de-enxame.html)
- [Desenvolvendo rotas inteligentes usando Otimização por Enxame de Partículas](https://medium.com/fcamara-hpt/desenvolvendo-rotas-inteligentes-usando-otimiza%C3%A7%C3%A3o-por-enxame-de-part%C3%ADculas-68085d1b43c0)
