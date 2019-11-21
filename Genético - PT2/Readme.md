### Atividade desenvolvida para a disciplina de Inteligência Artificial

#### Membros
[Helen França](https://github.com/helenfranca)
<br>[Júlia Miranda](https://github.com/juliamrc)

#### Implementação

Para a implementação do código com representação real, usamos a Mutação de Limite e o Crossover BLX-alfa.

##### Cromossomo

```python
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
```

##### População

```python 
def cria_populacao(numero_populacao):

    populacao = [
        Cromossomo(random.uniform(-20, 20)) for x in range(0, numero_populacao)
    ]
    return populacao
```


##### Torneio

```python 
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
```

##### Crossover e mutação

```python 
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
            # crossover blx-alfa

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
```

##### Elitismo

```python
def elitismo(nova_geracao, populacao):

    melhor_pai = sorted(populacao, key=Cromossomo.get_aptidao)[0]
    filhos_ordenados = sorted(nova_geracao, key=Cromossomo.get_aptidao, reverse=True)
    pior_filho = filhos_ordenados[0]
    indice = nova_geracao.index(pior_filho)

    if melhor_pai.get_aptidao() < pior_filho.get_aptidao():
        nova_geracao[indice] = melhor_pai
    return nova_geracao
```

##### Definindo melhor solução e média

```python
def media_melhores(melhores):
    media = []
    
    for i in range(geracao): #Quantidade de GERACOES
        media.append(0)
        for j in range(10): #Quantidade de EXECUCOES
            media[i] += melhores_melhores[j][i]
            media[i] /= 10

    return media

def melhor_solucao(melhores_melhores):
    pos_melhor = 0
    menor_aptidao = melhores_melhores[0][-1]
        
    for i in range(1, len(melhores_melhores)):
        if (menor_aptidao > melhores_melhores[i][-1]):
            menor_aptidao = melhores_melhores[i][-1]
            pos_melhor = i

    melhor_todas = melhores_melhores[pos_melhor]

    return melhor_todas
```

#### Resultados

![](https://github.com/helenfranca/inteligencia_artificial_disciplina/blob/mudan%C3%A7a_ag1/Gen%C3%A9tico%20-%20PT2/geracao10.png)

![](https://github.com/helenfranca/inteligencia_artificial_disciplina/blob/mudan%C3%A7a_ag1/Gen%C3%A9tico%20-%20PT2/geracao20.png)

##### Melhores resultados
- Aptidão para 10 gerações: -16.87601
- Média para 10 gerações : -16.41654 <br>

- Aptidão para 20 gerações: -16.87601
- Média para 20 gerações: -16.62771 

#### Comparação entre média: AG real e binário

Percebemos que no início da execução o valor da média no algoritmo binário está em valores longes do mínimo global (-16,785), enquanto no real já inicia em valores bem próximos. A medida que executamos mais vezes, o valor vai se aproximando cada vez mais do ideal, em ambos os casos. No final da execução, o algoritmo real tem melhor desempenho pois a média fica mais próxima ao valor que esperamos.

##### 10 gerações

- Binário: -11.48759, -11.27337, -13.25165, -14.22854, -14.84001, -14.7014, -14.81514, -14.86974, -14.9632, -15.2311.

- Real: -15.87467, -16.20164, -16.35509, -16.37196, -16,381, -16.38364, -16.38871, -16.40067, -16,.40777, -16.41654.

##### 20 gerações

- Binário: -11.6267, -12.73303, -14.19269, -14.76105, -14.96668, -15.45452, -15.5771, -15.70764, -15.74296, -15.65542, -15.69955, -15.7004, -15.81466, -15.82281, -16.47434, -16.52304, -16.52761, -16.52885, -16.52885, -16.51703.

- Real: -15.94188, -16.29765, -16.43104, -16.47841, -16.50296, -16.50513, -16.52127, -16.52478, -16.52645, -16.53874, -16.54021, -16.54091, -16.54106, -16.54152, -16.54177, -16.54194, -16.54245, -16.61754, -16.61755, -16.62771.


#### Rodando o algoritmo

##### Importante

É necessário ter Python3 instalado em sua máquina. Caso não tenha, [clique aqui](https://www.python.org/downloads/) e efetue os procedimentos.

- Faça um clone do projeto em sua IDE de preferência ou o download dos arquivos
- Por meio da linha de comando navegue até o diretório onde se encontram os arquivos-fonte

##### Via linha de comando, escreva:

- python geneticopt2.py


##### Lembre-se:

- Caso não possua os arquivos CSV na pasta em questão, o algoritmo irá criá-lo.


#### Referências

Aula e Slides









