# Discussão Teórica

`A justificativa da abordagem adotada na Questão 2 (escolha entre busca em profundidade e largura) deve ser redigida em formato texto e entregue em um arquivo Markdown separado.`

# Resposta:

O algoritmo implementado utiliza a exploração em profundidade (DFS), pois explora a árvore seguindo um caminho vertical, indo fundo em um ramo antes de explorar os outros ramos.

Esse método foi escolhido pois existe um único caminho a ser encontrado. Dessa forma, não é relevante priorizar a busca de um caminho mais curto.
A implementação considerou que não há ciclos. Por isso, armazena apenas o ramo que está sendo explorado no momento e suas bifurcações, não todos os vértices visitados, resultando em uma maior economia de memória.
