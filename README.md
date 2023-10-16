<h1 align="center"><b><i>Graph search</i></b></h1>

<p align ="center">
    <img src="GRAPHSEARCH.png" style= "width: 60%; height: auto;" align="right" />
</p>


#### Docente:
- [Kennedy Reurison Lopes](https://github.com/kennedyufersa)

#### Monitor:
- [Marcos Mikael Lima Vidal](https://github.com/Bazchh)

#### Discentes:
- [Abner Gama Torres](https://github.com/bnerTT)
- [Caio Moisés Vieira Cavalcante](https://github.com/caiomoises)
- [Francisco Gerliano de Oliveira Souza](https://github.com/sgerliano)
- [Vladimyr de Oliveira Guedes](https://github.com/vladguedes)

## INTRODUÇÃO

Grafos são estruturas de dados que representam conjuntos de elementos, chamados nós ou vértices, os quais são unidos por outros elementos chamados arestas. Um exemplo de utilização de grafos em abstrações do cotidiano pode ser a presentação de cidades sendo nós e as estradas que as conectam sendo arestas.

Este código tem como objetivo criar um grafo matricial das cidades no estado do Rio
Grande do Norte (RN) com base nas coordenadas de latitude e longitude (GPS) de cada cidade.
O grafo representa as relações de vizinhança entre as cidades, onde duas cidades são
consideradas vizinhas se a distância entre elas for menor que um determinado valor
especificado. Este projeto é valioso para análises geoespaciais, urbanas e de planejamento, pois
permite identificar quais cidades são vizinhas, calcular métricas como a cidade com mais
vizinhos e determinar distâncias mínimas e máximas para que as cidades sejam consideradas
vizinhas.

- Exemplo:
  
    Para ilustrar o funcionamento do código, suponhamos que temos um conjunto de
cidades no RN, cada uma com suas coordenadas GPS (latitude e longitude). Queremos
determinar quais cidades são vizinhas considerando que a distância máxima para a vizinhança
seja de 0.1 unidades de distância geoespacial. O código criará um grafo matricial onde as
cidades serão nós e as arestas entre elas indicarão que são vizinhas se a distância entre elas for
menor que 0.1. Além disso, o código calculará métricas como a cidade com mais vizinhos,
cidades sem vizinhos e as distâncias mínimas e máximas necessárias para que as cidades sejam
consideradas vizinhas ou não. Essas informações podem ser fundamentais para planejamento
urbano, logística e análises territoriais no estado do RN.

    Neste relatório, examinaremos detalhadamente a implementação do código, incluindo
as funções em Python que o compõem e a lógica por trás da criação do grafo matricial. Também
descreveremos os testes realizados, apresentando resultados e discutindo como esses resultados
atendem aos objetivos definidos. Além disso, abordaremos os desafios encontrados durante o
desenvolvimento e as soluções adotadas. No final, resumiremos o projeto e destacaremos o
aprendizado obtido ao criar essa ferramenta de análise geoespacial no contexto do RN.

## DESCRIÇÃO GERAL DO CÓDIGO
O código é voltado para o processamento de dados relacionados a cidades do estado do
Rio Grande do Norte. Ele lê informações de coordenadas geográficas (latitude e longitude) e
nome de cidades a partir de arquivos CSV, calcula as distâncias entre todas as cidades e gera
um grafo matricial que representa essas distâncias.

O código inclui funções para calcular a distância entre as cidades, identificar cidades
com mais vizinhos, encontrar cidades sem vizinhos, determinar a distância mínima para que
todas as cidades sejam vizinhas e a distância máxima para que nenhuma cidade seja vizinha.

## VISÃO GERAL
O código é dividido em várias funções, cada uma com uma tarefa específica. Ele começa
alocando uma matriz para representar o grafo e, em seguida, calcula a distância entre as cidades
com base nas coordenadas geográficas. Depois, o código realiza várias análises para identificar
cidades com mais vizinhos, cidades sem vizinhos e métricas de distância.

## FUNÇÕES EM PYTHON
- ‘alocaMatriz’: Aloca uma matriz para representar o grafo.
- ‘RN’: Retorna um subconjunto de cidades pertencentes ao Rio Grande do Norte.
- ‘criarGrafo’: Cria uma matriz para representar o grafo.
- ‘calculaDistancia’: Calcula a distância entre as cidades e preenche a matriz do grafo.
- ‘printCidadeComMaisVizinhos’: Imprime a cidade do RN com mais vizinhos.
- ‘printCidadeSemVizinhos’: Imprime cidades do RN que não têm vizinhos.
- ‘printDistTodasVizinhas’: Imprime a distância necessária para que todas as cidades sejam vizinhas.
- ‘printDistMinTodasVizinhas’: Imprime a distância necessária para que nenhuma cidade seja vizinha.
- ‘printDistMaxNenhumVizinhas’: Imprime a distância necessária para que todas as cidades sejam vizinhas.
- ‘printGrafoMatricial’: Imprime uma representação visual do grafo matricial.

## LOGICA PRINCIPAL
A lógica principal envolve a alocação de uma matriz, o cálculo de distâncias, a
identificação de cidades com mais vizinhos e a análise de distâncias mínimas e máximas para
estabelecer relações de vizinhança.

## TESTES E RESULTADOS
Foram realizados vários testes para verificar a funcionalidade do código e analisar as
relações de vizinhança entre as cidades do estado do Rio Grande do Norte (RN) com base nas
distâncias calculadas a partir das coordenadas GPS. Os testes envolveram diferentes valores de
distância (D) para determinar as cidades vizinhas e aplicaram métricas para identificar as
cidades com mais vizinhos.
    Resultados dos Testes:

- Teste 1: Identificação da Cidade com Mais Vizinhos
    - Distância (D) = 0.05
    - Resultado: A cidade de Natal tem 7 vizinhos.
- Teste 2: Identificação de Cidades Sem Vizinhos
    - Distância (D) = 0.2
    - Resultado: Todas as cidades têm pelo menos um vizinho.
- Teste 3: Distância Necessária para Todas as Cidades Serem Vizinhas
    - Resultado: É necessária uma distância de 0.04972 para que todas as cidades sejam
    vizinhas.
- Teste 4: Distância Necessária para Nenhuma Cidade Ser Vizinha
    - Resultado: É necessária uma distância de 0.15508 para que nenhuma cidade seja
    vizinha.
Os testes demonstraram que o código é eficaz na criação do grafo matricial das cidades
do RN com base em distâncias calculadas a partir das coordenadas GPS. A identificação da
cidade com mais vizinhos e a análise das cidades sem vizinhos podem ser valiosas para tomadas
de decisões urbanas e planejamento. Além disso, as métricas de distância fornecem informações
úteis para determinar quais cidades são consideradas vizinhas ou não. O código atende aos
objetivos definidos e pode ser uma ferramenta útil para análises geoespaciais no estado do RN.

## DESAFIOS E SOLUÇÕES
Durante o desenvolvimento deste código, alguns desafios foram identificados e
superados para garantir que o grafo matricial das cidades vizinhas no RN fosse criado com
precisão. Abaixo, destacamos os principais desafios encontrados e as soluções adotadas:

#### 1. Leitura de Dados a partir de Arquivos CSV:
 - Um dos principais desafios foi ler as informações das cidades e suas coordenadas GPS
a partir de arquivos CSV, que não estavam em um formato diretamente compatível com o
Python. Para superar esse desafio, foi necessário analisar e tratar esses arquivos de maneira
eficaz.

- Solução: Utilizamos a biblioteca `csv` do Python para fazer a leitura dos arquivos
CSV e transformar os dados em objetos Python. O código foi adaptado para interpretar as
informações corretamente, convertendo strings em tipos de dados apropriados.

#### 2. Cálculo de Distâncias Geoespaciais:
- Graph Search Página 5
- Calcular a distância entre duas cidades com base nas coordenadas GPS foi um desafio,
pois envolveu cálculos matemáticos complexos para obter a distância em unidades
geoespaciais.
     
- Solução: Implementamos uma função para calcular a distância geoespacial entre as
cidades usando a fórmula da distância euclidiana no plano cartesiano. Esta solução permitiu a
conversão de coordenadas GPS em distâncias em unidades padronizadas para comparação.

#### 3. Construção do Grafo Matricial:    
- A construção do grafo matricial envolveu a criação de uma matriz que representasse
as relações de vizinhança entre as cidades com base nas distâncias calculadas. Garantir que essa
matriz fosse preenchida corretamente foi um desafio.

- Solução: Criamos uma função dedicada para preencher a matriz do grafo,
considerando as distâncias calculadas entre as cidades. Também definimos critérios claros para
determinar quando duas cidades são vizinhas ou não com base na distância máxima
especificada.

Essas soluções permitiram superar os desafios identificados durante o desenvolvimento
do código e garantir a criação precisa do grafo matricial que representa as relações de
vizinhança entre as cidades no RN. O projeto foi concluído com sucesso, permitindo análises
geoespaciais valiosas.

## CONCLUSÃO
Este código em Python permite a análise de relações de vizinhança entre cidades do RN
com base em coordenadas geográficas. Ele fornece informações sobre cidades com mais
vizinhos, cidades sem vizinhos e métricas de distância mínima e máxima para que as cidades
sejam consideradas vizinhas. O código pode ser uma ferramenta útil para análises geoespaciais
e planejamento urbano no estado do Rio Grande do Norte.

## CÓDIGO FONTE
[Link para repositório no GitHub:](https://github.com/caiomoises/graph_search).

## CLONANDO O CÓDIGO
o Abra o seu Visual Studio Code (caso não tenha instalado, faça download no link:
(https://code.visualstudio.com/download)

o Com o VsCode aberto, vá na opção ‘Terminal’ e ‘New Terminal’, com o
terminal aberto, configure o Git usando os seguintes comandos:
Graph Search Página 6

    ▪ git config --global user.name “seu nome aqui”
    ▪ git config --global user.email “seu email aqui”
    
o Após o Git esta configurado, execute o seguinte comando para clonar o
repositório:

    ▪ git clone https://github.com/caiomoises/collisionHash.git
    
o Depois disso, você terá acesso ao código fonte.

o Para executá-lo, abra novamente o terminal e digite o seguinte comando:

    ▪ python3 main.py
    
o Após o código ser compilado siga os passos descritos no tópico ‘TESTES E RESULTADOS’

## REFERÊNCIAS
o https://www.youtube.com/watch?v=4-1fG04nQGI

o https://www.youtube.com/watch?v=IzG9l_7GaZM 