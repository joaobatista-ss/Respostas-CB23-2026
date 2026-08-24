
## Questão 01 - Identifique relações de herança entre as classes.
**Explique como as classes poderiam ser organizadas em uma hierarquia de herança, indicando quais classes seriam classes base e quais seriam subclasses, e descreva o que seria herdado em cada caso.

As classes bases seriam: Pessoa, Iguaria e Restaurante.

Funcionario seria a primeira subclasse de Pessoa. Herda os atributos nome e idade.
Garcom, ChefeDeCozinha e Gerente são subclasses de Funcionario. Herdam os atributos nome, idade, salario e carga_horaria.

As classes Pizza e Bolo herdam são subclasses de Iguaria, e herdam os atributos nome e preco.

A classe Pizzaria é subclasse de Restaurante, e herda os atributos nome, endereco e telefone.


Hierarquia de herança mostrada por tabulação:
Pessoa (nome:str, idade:int)
	Funcionario (salario:float, carga_horaria:int)
		Garcom (anotar_pedido())
		Chefe de Cozinha (preparar())
		Gerente (demitir())

Iguaria (nome:str, preco:float)
	Pizza (borda_recheada:bool)
	Bolo (formato:str)

Restaurante (nome:str, endereco:str, telefone:str)
	Pizzaria (rodizio:bool)



## Questão 02 - Como você modelaria a relação entre a classe Restaurante e a classe Iguaria?
**Explique como essa relação seria implementada. Se necessário, sugira a criação de novos atributos ou até mesmo de novas classes para representar essa relação de forma eficiente.

Os atributos de Restaurante são nome, endereco e telefone e os atributos de Iguaria são nome e preco.
Essas duas classes não precisam de uma relação hierárquica entre elas. Endereco e telefone não são atributos adequados para serem herdados por Iguaria; e preco da classe Iguaria não é atributo adequado para ser herdado por Restaurante.
O atributo nome já existe nessas duas classes.

Sugestões:
- Desenvolver novos atributos independentes entre essas duas classes;
- Criar na classe Restaurante uma lista chamada cardápio para armazenar as Iguarias disponíveis (cardápio:list\[Iguaria]).


## Questão 03 - Indique os tipos que você atribuiria para os argumentos: argumento1, argumento2, argumento3
**Explique quais seriam os tipos apropriados para cada argumento com base no seu uso e na função em que são empregados. Considere se eles seriam, por exemplo, tipos primitivos, instâncias de classes, ou listas, e justifique sua escolha.

argumento1: Tipo Lista, pois um pedido de um cliente pode conter mais de um item. Os elementos esperados dentro da lista devem ser subclasses de Iguaria, como Pizza ou Bolo.

argumento2: Tipo Lista, pois em geral um Chefe de Cozinha coordena o preparo de vários pratos simultaneamente. É esperado que os elementos dentro da lista sejam subclasses de Iguaria.

argumento3: Tipo Funcionario ou qualquer outro tipo que herdar de Funcionario.
Pois para demitir alguém é preciso que seja funcionário, portanto, é preciso que o tipo contenha todos os atributos da classe Funcionario.

Os três casos precisam ser elementos já instanciados, para que faça sentido.
Nenhum deles deve ser do tipo primitivo, pois não são itens suficientemente especificados: não possuem todas as características importantes dado que o contexto é realizar uma demissão.