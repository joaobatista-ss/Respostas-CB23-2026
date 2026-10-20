## Marco 1
Resolve as issues #1 a #5 do enunciado.

### O que mudou
- Em Issue 1:
  - Definição de Expressão Regular para parsear o log
  - Implementação de ler_log, valida_tag, contagem_por_tag, serie
- Em Issue 2:
  - Implementação de criar_conversores
  - Identificação e correção de problema: Late binding
- Em Issue 3:
  - Implementação de medir_memoria e medir_tempos
  - Previsão e medição de o espaço e tempo gasto em armazenamento e acesso de um milhão de contagens em diferentes coleções/estruturas
- Em issue 4:
  - Correção de Bug em test_dados
  - Implementação de mais testes unitários (unittest)
- Em issue 5:
  - Implementação de SerieTemporal.reamostrar

### Como testei
- `python -m unittest discover -v`: Ran 38 tests in 0.060s OK
Executa 38 testes, e todos eles passam.

- `python marco1.py`: todos os assert passam.
Marco 1: todos os assert passaram.

### Pontos de atenção para o revisor
- ...
