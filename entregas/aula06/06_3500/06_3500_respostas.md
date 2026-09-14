# Respostas - Aula Prática 6

## Análise de Complexidade: Fila com Duas Pilhas

`No arquivo de respostas, explique por que desenfileirar pode custar O(N) em uma chamada isolada e ainda assim ser O(1) amortizada (caso médio), argumentando sobre quantas vezes cada elemento é transferido entre as duas pilhas ao longo de sua vida na estrutura.`

## Resposta

A operação desenfileirar() pode apresentar custo O(N) em uma chamada isolada, mas sua complexidade amortizada é O(1).

A coleção utiliza uma estratégia de armazenar os elementos de maneira distribuída em duas pilhas (sejam A e B) da seguinte maneira:

Uma pilha A é utilizada para inserção dos elementos e uma pilha B é utilizada para retirada de elementos.
Quando é preciso acessar o elemento (por meio de desenfileirar() ou frente()), a estrutura busca pelo elemento da pilha B.
Se a pilha B estiver vazia ele transfere cada um dos elementos da pilha A para a pilha B, de modo que a pilha B fique com os elementos inversamente ordenados. Nessa situação isolada a operação de transferência das pilhas apresenta um custo O(N), porém, o acesso ao elemento da frente pode ser feito com custo O(1) pela pilha B, até que a mesma se esvazie novamente.

Considerando apenas as operações enfileirar, desenfileirar e frente, o ciclo de vida de um elemento é:

- ser inserido na pilha A;
- ser transferido para a pilha B;
- ser excluído da pilha B.

Note que um elemento é transferido da pilha A para a pilha B exatamente uma única vez. E cada uma dessas operações em seu ciclo de vida tem custo O(1).

Desse modo, apesar de uma operação de acesso isolada poder ter custo O(N), cada elemento individualmente tem custo O(1) ao longo de sua vida na estrutura.
