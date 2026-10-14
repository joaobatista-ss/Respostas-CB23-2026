# Relatório — João Batista de Sousa Silva (3500)

Relatório do projeto, preenchido na sua branch. Cada marco acrescenta a sua seção. Responda com as suas palavras e com
os números da sua execução; cada resposta cabe em até 6 linhas, além das tabelas.

## Marco 1

### Ambiente

<!-- Cole aqui a saída de `which python` e da Etapa 0 do `python marco1.py`. -->

D:\Projetos\IMPATech\Programacao_2\Respostas-CB23-2026\.venv\Scripts\python.exe

=== Etapa 0: ambiente ===
Python 3.12.10 | NumPy 2.5.3 | fornecido 1.0

### R1 — Expressões regulares

<!-- Uma string que re.match aceita e re.fullmatch rejeita com o padrão de tag; consequência para valida_tag. -->

" PT101", é aceita por re.match, pois a expressão regular "[A-Z]{1,2}\d{1,3}" é encontrada. Porém, re.fullmatch a rejeita, pois é verificado se a string inteira corresponde a expressão regular, e um caracter em branco no começo torna a string incompatível com o padrão.

### R2 — Linhas inválidas

<!-- Por que ler_log devolve as linhas descartadas; uma situação real em que descartar em silêncio esconderia um problema. -->
ler_log devolve as linhas inválidas para que não se perca a informação de que há sensores defeituosos.
Descartar em silêncio as linhas inválidas impossibilita a verificação da integridade total das informações recebidas.

Podemos exemplificar com uma situação em que um sensor se desconecta.
Várias linhas, como "### falha de comunicacao com a RTU ###", serão registradas no log, porém, caso o leitor de log apenas ignore todas elas, ninguém saberá do problema e o mesmo poderá não ser resolvido.

### R3 — Late binding

<!-- Por que errados["PT102"](4095) dá 409,5 e por que a sua criar_conversores não tem o problema. -->
Ao implementar a função lambda como (`lambda c : c \* k`), a variável c será parâmetro de lambda, mas a variável k - que não é parâmetro - será a que estiver definida no escopo e no momento em que a função for chamada.
O laço for modifica a variável k a cada iteração, e na última volta o valor de k fica definido como 0.1, pelo que a função lambda fará 4095 \* 0,1 e isso dá 409,5.

A função criar_conversores não possui esse problema, porque cria lambda's como (`lambda c k_=k: c * k_`).
Dessa forma, o valor de k estará definido no dentro do escopo da função lambda, e não no escopo externo.

### R4 — Escala nominal

<!-- Hipótese para a diferença da Etapa 2(f) e onde, no código da base, está a explicação. -->
O valor de 'Pressão Recalque' retornado no dicionário de verdade é sempre o valor que está definido na linha 25 do arquivo 'simulador.py', como 'PRESSAO_RECALQUE = 380.0  # pressão de recalque em operação (kPa)'.
O dicionário de verdade inclui o par: '"pressao_recalque": PRESSAO_RECALQUE'. Portanto, em todas as execuções, pressao_recalque é definido como 380.0 e não é alterado posteriormente.

### R5 — Previsão × medição (Etapa 3)

Previsões registradas no commit: <!-- cole o hash curto do commit de previsões -->

| Grandeza | Previsão | Medido |
| --- | --- | --- |
| Memória da lista / memória do `uint16` | 14 | |
| Tempo do laço / tempo vetorizado | 14 | |
| Tempo da compreensão / tempo do laço | 1 | |

<!-- Explique a maior diferença entre previsão e medição; por que uint16 * 20 dá 16364; que dtype você escolheria para contagens e para kPa. -->

### R6 — Tipos da SerieTemporal (Etapa 4d)

| Expressão | Tipo previsto | Tipo observado |
| --- | --- | --- |
| `s + s` | | |
| `s[1:]` | | |
| `s * 2` | | |
| `s.sum()` | | |
| `s[0]` | | |

<!-- Explique o resultado que mais surpreendeu você. -->

### R7 — Issue #4

<!-- Sintoma; o teste de regressão (nome); a causa, em termos da soma acumulada; a correção; por que os testes de aceitação não pegaram o defeito; mais um caso que eles não cobrem e qual teste seu o cobre. -->
