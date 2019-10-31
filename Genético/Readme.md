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

------

#### Implementação

#### Classe Cromossomo

```python
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
```

#### Seleção Torneio
Processo em que se escolhe aleatoriamente dois pais para gerarem filhos
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
#### Crossover
Processo onde acontece o cruzamento dos pais, gerando dois novos filhos. Optamos nesse processo que a acad novo filho gerado ele já passe pelo processo de mutação e atualize sua aptidão. Lembrando que o prórpio cromossomo sabe calcular sua aptidão e também fazer mutação.<br>
Obs.: Encontramos um melhor resultado quando mudamos a taxa de crossover para 90%.

```python
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
```

#### Elitismo
Nesse processo busca-se o melhor pai e caso ele seja melhor do que o pior filho, esse filho é substituído.

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

#### Programa principal

```python
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

            escreve_arquivo(conteudo_arquivo(melhores_melhores), geracao)

```
----
#### Resultados

Abaixo estão os resultados obtidos em cada um dos testes:

![](https://github.com/helenfranca/Inteligencia_Artificial_Disciplina/blob/master/Genetico/Geracao_10.png?raw=true)

![](https://github.com/helenfranca/Inteligencia_Artificial_Disciplina/blob/master/Genetico/Geracao_20.png?raw=true)

Melhor resultado de aptidão para 10 gerações: -16.87594 <br>
Melhor resultado de aptidão para 20 gerações: -16.87594

#### Rodando o algoritmo

##### Importante

É necessário ter Python3 instalado em sua máquina. Caso não tenha, [clique aqui](https://www.python.org/downloads/) e efetue os procedimentos.

- Faça um clone do projeto em sua IDE de preferência ou o download dos arquivos
- Por meio da linha de comando navegue até o diretório onde se encontram os arquivos-fonte

##### Via linha de comando, escreva:

- python genetico.py


##### Lembre-se:

- Caso não possua os arquivos CSV na pasta em questão, o algoritmo irá criá-lo.


#### Referências

Aula e Slides
