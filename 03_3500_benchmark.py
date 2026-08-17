"""
Testes comparativos de tempo de execução (benchmarking) entre diferentes algoritmos de ordenação

Realiza testes nos algoritmos selection_sort, divide_and_conquer_sort e quick_sort importados de AP_03_ordenacao.
Funcionamento:
    - Gera K listas com n elementos para cada valor em N;
    - Os resultados dos testes são armazenados em 3 dicionários
    - Os resultados são plotados em um gráfico usando matplotlib

Requisitos:
  - matplotlib
"""

from AP_03_ordenacao import *
import time
import random
import sys
import copy
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.lines as mlines


N = [i*50 for i in range(1, 21)]  # Lista de casos de teste
K = 50

sys.setrecursionlimit(2**31 - 1)


def medir_tempo_de_ordenacao(lista, algoritmo):
    """Mede o tempo de execução de um algoritmo de ordenação para uma lista fornecida.

    Args:
        lista (List[List]): A lista com as listas a serem ordenadas.
        algoritmo (Callable): A função responsável por realizar a ordenação da lista.

    Returns:
        float: O tempo MÉDIO decorrido para concluir a ordenação, em segundos.
    """

    lista = copy.deepcopy(lista)

    start_time = time.perf_counter()
    for l in lista:
        algoritmo(l)
    end_time = time.perf_counter()

    print(f"Algorítimo: {algoritmo.__name__}; Tempo: {end_time - start_time} s")
    return (end_time - start_time)/K


def plotar_grafico(
        r_aleatorias:dict,
        r_inv_ordenadas:dict,
        r_ordenadas:dict
):
    fig, ax = plt.subplots()
    fig.set_size_inches(8, 5)

    ax.plot(r_aleatorias["selection_sort"].keys(), r_aleatorias["selection_sort"].values(), marker="o", color="red", linestyle="-", label="selection_sort, lista aleatória", linewidth=2)
    ax.plot(r_inv_ordenadas["selection_sort"].keys(), r_inv_ordenadas["selection_sort"].values(), marker="o", color="red", linestyle="--", label="selection_sort, lista inv_ordenada", linewidth=2)
    ax.plot(r_ordenadas["selection_sort"].keys(), r_ordenadas["selection_sort"].values(), marker="o", color="red", linestyle=":", label="selection_sort, lista ordenada", linewidth=2)

    ax.plot(r_aleatorias["divide_and_conquer_sort"].keys(), r_aleatorias["divide_and_conquer_sort"].values(), marker="o", color="blue", linestyle="-", label="divide_and_conquer_sort, lista aleatória", linewidth=2)
    ax.plot(r_inv_ordenadas["divide_and_conquer_sort"].keys(), r_inv_ordenadas["divide_and_conquer_sort"].values(), marker="o", color="blue", linestyle="--", label="divide_and_conquer_sort, lista inv_ordenada", linewidth=2)
    ax.plot(r_ordenadas["divide_and_conquer_sort"].keys(), r_ordenadas["divide_and_conquer_sort"].values(), marker="o", color="blue", linestyle=":", label="divide_and_conquer_sort, lista ordenada", linewidth=2)

    ax.plot(r_aleatorias["quick_sort"].keys(), r_aleatorias["quick_sort"].values(), marker="o", color="green", linestyle="-", label="quick_sort, lista aleatória", linewidth=2)
    ax.plot(r_inv_ordenadas["quick_sort"].keys(), r_inv_ordenadas["quick_sort"].values(), marker="o", color="green", linestyle="--", label="quick_sort, lista inv_ordenada", linewidth=2)
    ax.plot(r_ordenadas["quick_sort"].keys(), r_ordenadas["quick_sort"].values(), marker="o", color="green", linestyle=":", label="quick_sort, lista ordenada", linewidth=2)

    ax.set_title("Gráfico do tempo de execução")
    ax.set_ylabel("Tempo médio de execução (s)\n")
    ax.set_xlabel("Tamanho da entrada")

    legenda = [
        mpatches.Patch(color="red", label="selection_sort"),
        mpatches.Patch(color="blue", label="divide_and_conquer_sort"),
        mpatches.Patch(color="green", label="quick_sort"),
        mlines.Line2D([0], [0], color="black", linestyle="-", label="Lista Aleatória"),
        mlines.Line2D([0], [0], color="black", linestyle="--", label="Lista Inversamente Ordenada"),
        mlines.Line2D([0], [0], color="black", linestyle=":", label="Lista Ordenada"),
    ]

    plt.legend(handles=legenda, loc="upper left")

    plt.show()


if __name__ == "__main__":
    """Executa os testes nos três algoritmos para cada valor n da lista de casos de testes N"""

    # cria estruturas para armazenar os resultados dos testes:
    resultados_listas_aleatorias:dict[dict] = {"selection_sort":{}, "divide_and_conquer_sort":{}, "quick_sort":{}}
    resultados_listas_inv_ordenadas:dict[dict] = {"selection_sort":{}, "divide_and_conquer_sort":{}, "quick_sort":{}}
    resultados_listas_ordenadas:dict[dict] = {"selection_sort":{}, "divide_and_conquer_sort":{}, "quick_sort":{}}

    # executa testes
    for n in N:
        # cria K listas com n elementos
        listas = [[random.randint(100, 10**5) for _ in range(n)] for _ in range(K)]


        print(f"\n" + "#"*60)
        print(f"Tamanho das listas (n): {n}; quantidade de listas (K): {K}\n")
        print(f"Realizando testes com listas desordenadas: ")
        selection_sort_time = medir_tempo_de_ordenacao(listas, selection_sort)
        divide_and_conquer_sort_time = medir_tempo_de_ordenacao(listas, divide_and_conquer_sort)
        quick_sort_time = medir_tempo_de_ordenacao(listas, quick_sort)

        # armazena resultados
        resultados_listas_aleatorias["selection_sort"][n] = selection_sort_time
        resultados_listas_aleatorias["divide_and_conquer_sort"][n] = divide_and_conquer_sort_time
        resultados_listas_aleatorias["quick_sort"][n] = quick_sort_time


        print()
        print(f"Realizando testes com listas inversamente ordenadas: ")
        listas = [divide_and_conquer_sort(lista)[::-1] for lista in listas]
        
        selection_sort_time = medir_tempo_de_ordenacao(listas, selection_sort)
        divide_and_conquer_sort_time = medir_tempo_de_ordenacao(listas, divide_and_conquer_sort)
        quick_sort_time = medir_tempo_de_ordenacao(listas, quick_sort)

        # armazena resultados
        resultados_listas_inv_ordenadas["selection_sort"][n] = selection_sort_time
        resultados_listas_inv_ordenadas["divide_and_conquer_sort"][n] = divide_and_conquer_sort_time
        resultados_listas_inv_ordenadas["quick_sort"][n] = quick_sort_time


        print()
        print(f"Realizando testes com listas já ordenadas: ")
        listas = [divide_and_conquer_sort(lista) for lista in listas]
        
        selection_sort_time = medir_tempo_de_ordenacao(listas, selection_sort)
        divide_and_conquer_sort_time = medir_tempo_de_ordenacao(listas, divide_and_conquer_sort)
        quick_sort_time = medir_tempo_de_ordenacao(listas, quick_sort)

        # armazena resultados
        resultados_listas_ordenadas["selection_sort"][n] = selection_sort_time
        resultados_listas_ordenadas["divide_and_conquer_sort"][n] = divide_and_conquer_sort_time
        resultados_listas_ordenadas["quick_sort"][n] = quick_sort_time

    # plota o gráfico com os resultados
    plotar_grafico(
        resultados_listas_aleatorias,
        resultados_listas_inv_ordenadas,
        resultados_listas_ordenadas
    )