### Atividade desenvolvida para a disciplina de Inteligência Artificial

#### Membros
[Helen França](https://github.com/helenfranca)
<br>[Júlia Miranda](https://github.com/juliamrc)

#### O Algoritmo Genético

Os Algoritmos Genéticos (AG) foram concebidos em 1960 por John Holland (Holland 1975), com o objetivo inicial de estudar os fenômenos relacionados à adaptação das espécies e da seleção natural que ocorre na natureza (Darwin 1859), bem como desenvolver uma maneira de incorporar estes conceitos aos computadores (Mitchell 1997).

Os AGs possuem uma larga aplicação em muitas áreas científicas, entre as quais podem ser citados problemas de otimização de soluções, aprendizado de máquina, desenvolvimento de estratégias e fórmulas matemáticas.

A idéia básica de funcionamento dos algoritmos genéticos é a de tratar as possíveis soluções do problema como "indivíduos" de uma "população", que irá "evoluir" a cada iteração ou "geração". 

A execução do algoritmo pode ser resumida nos seguintes passos:

- Inicialmente escolhe-se uma população inicial, normalmente formada por
indivíduos criados aleatoriamente;

- Avalia-se toda a população de indivíduos segundo algum critério, determinado
por uma função que avalia a qualidade do indivíduo (função de aptidão ou
"fitness");

- Em seguida, através do operador de "seleção", escolhem-se os indivíduos de
melhor valor (dado pela função de aptidão) como base para a criação de um
novo conjunto de possíveis soluções, chamado de nova "geração";

- Esta nova geração é obtida aplicando-se sobre os indivíduos selecionados
operações que misturem suas características (chamadas "genes"), através dos
operadores de "cruzamento" ("crossover") e "mutação";

- Estes passos são repetidos até que uma solução aceitável seja encontrada, até
que o número predeterminado de passos seja atingido ou até que o algoritmo
não consiga mais melhorar a solução já encontrada. 

#### Problema proposto
Utilizar um algoritmo genético binário para minimizar a função descrita abaixo.

                                                f(x) = cos(x)*x + 2


#### Implementação

#### Classe Cromossomo

```python
  class Cromossomo:
    def __init__(self, corpo):
        self.corpo = corpo
        
        # Normaliza
        dec = bin2Dec(formata(self.corpo))
        self.x = (-20) + (20 + 20) * (dec / (pow(2,10) - 1))
        
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
        self.x = (-20) + (20 + 20) * (dec / (pow(2,10) - 1))
        self.aptidao = math.cos(self.x) * self.x + 2
```

#### Seleção Torneio

```python
  def selecao_torneio(populacao):
    pais = []
    

    for _ in range(0,len(populacao)):
        a = random.choice(populacao) # Pega um cromossomo 
        b = random.choice(populacao) # Pega um cromossomo

    # Verifica quem é menor. O menor se torna um pai para a nova geração
        if (a.get_aptidao() < b.get_aptidao()):
            pai = a
        else:
            pai = b

        pais.append(pai)
    
    return pais
```
#### Crossover

```python
  def crossover(pais):
    nova_geracao = []
    tam = 0
    while tam < len(pais):
        taxa_cross = random.uniform(0,1) * 100

        paiUm = pais[tam]
        paiDois = pais[tam + 1]

        if taxa_cross <= 60 :
            #Cruzamento
            corte = random.randrange(1,10)
            cromossomo_pai_um = paiUm.get_corpo()
            cromossomo_pai_dois = paiDois.get_corpo()

            filhoUm = cromossomo_pai_um[0:corte] + cromossomo_pai_dois[corte:]
            filhoDois = cromossomo_pai_dois[0:corte] + cromossomo_pai_um[corte:]

            filhoUm = Cromossomo(filhoUm)
            filhoDois = Cromossomo(filhoDois)
            
        else:
            filhoUm = paiUm
            filhoDois = paiDois

        nova_geracao.append(filhoUm)
        nova_geracao.append(filhoDois) 
        tam = tam + 2

    return nova_geracao
```

#### Mutação

```python
  def mutacao(nova_geracao):
    for filho in nova_geracao:
        cromossomo = filho.get_corpo()
        
        for i in range(0,len(cromossomo)):
            taxa_mutacao = random.randrange(0,2)
            if(taxa_mutacao == 1):
                if(cromossomo[i] == 0):
                    cromossomo[i] = 1
                else:
                    cromossomo[i] = 0
        filho.atualiza()
```

#### Elitismo

```python
  def elitismo(nova_geracao, populacao):
    
    melhor_pai = sorted(populacao, key=Cromossomo.get_aptidao)[0]
    filhos_ordenados = sorted(nova_geracao, key=Cromossomo.get_aptidao)
    melhor_filho = filhos_ordenados[0]
    indice = nova_geracao.index(melhor_filho)
    
    if melhor_pai.get_aptidao() < melhor_filho.get_aptidao():
        nova_geracao[indice] = melhor_pai
```


falta o main()


#### Resultados



#### Rodando o algoritmo


________________
#### Referências
Aula AG disponibilizada no AVA
