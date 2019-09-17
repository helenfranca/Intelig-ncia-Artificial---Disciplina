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

Há também um segundo ‘crossover’ para cada indivíduo. Porém, nesse, nós misturamos a rota atual de cada indivíduo com a melhor rota já obti-
da pelo mesmo, anteriormente (chamamos de **pbest**).

#### A cada iteração...
1. Escolhemos o líder, dentre os indivíduos. (O que tem melhor resultado).
2. Fazemos um ***crossover*** de cada indivíduo com seu **pbest**.
3. Com a rota resultante fazemos um outro crossover, mas com o **gbest**.





#### Referências
- [Introdução à Inteligência de Enxame](http://aimotion.blogspot.com/2009/04/introducao-inteligencia-de-enxame.html)
- [Desenvolvendo rotas inteligentes usando Otimização por Enxame de Partículas](https://medium.com/fcamara-hpt/desenvolvendo-rotas-inteligentes-usando-otimiza%C3%A7%C3%A3o-por-enxame-de-part%C3%ADculas-68085d1b43c0)
