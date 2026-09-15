from copy import deepcopy
from pprint import pprint
from time import sleep

# python 3

"""
maze_builder.py
---------------
Geração procedural de labirintos perfeitos usando busca em profundidade (DFS)
com retrocesso (backtracking).

Um labirinto "perfeito" possui exactamente um caminho entre quaisquer dois
pontos — equivalente a uma árvore geradora aleatória sobre a grade m x n.

Representação interna
~~~~~~~~~~~~~~~~~~~~~
A grade lógica de m linhas X n colunas é expandida para uma matriz de
(2m+1) X (2n+1) células, onde:
  - células de coordenadas ímpares (2i+1, 2j+1) representam salas (rooms);
  - células entre duas salas adjacentes representam paredes derrubáveis;
  - as bordas externas são sempre paredes.

O queijo (cheese) é colocado aleatoriamente em qualquer sala.
"""

import random


def generate_maze(m, n, room=0, wall=1, cheese='.'):
    """Gera um labirinto perfeito de m X n células usando DFS com backtracking.

    Parameters
    ----------
    m : int
        Número de linhas da grade lógica.
    n : int
        Número de colunas da grade lógica.
    room : int or str, optional
        Valor usado para representar passagens abertas. Padrão: 0.
    wall : int or str, optional
        Valor usado para representar paredes. Padrão: 1.
    cheese : str, optional
        Símbolo colocado aleatoriamente em uma sala como objetivo. Padrão: '.'.

    Returns
    -------
    list[list]
        Matriz (2m+1) X (2n+1) representando o labirinto gerado.
    """
    # Inicializa a matriz expandida com todas as células como parede
    maze = [[wall] * (2 * n + 1) for _ in range(2 * m + 1)]
    # print(maze)

    # Deslocamentos para os quatro vizinhos cardeais: N, S, W, E
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Abre passagem iterativamente a partir da sala (x, y)
    x, y = 0, 0
    stack = [(x, y, random.sample(directions, len(directions)))]
    while stack:
        x, y, _directions = stack[-1]

        if not _directions:
            stack.pop()
            continue

        maze[2 * x + 1][2 * y + 1] = room

        dx, dy = _directions.pop()
        nx, ny = x + dx, y + dy
        if 0 <= nx < m and 0 <= ny < n and maze[2 * nx + 1][2 * ny + 1] == wall:
            # Derruba a parede entre (x,y) e (nx,ny)
            maze[2 * x + 1 + dx][2 * y + 1 + dy] = room
            print_maze(maze)
            stack.append((nx, ny, random.sample(directions, len(directions))))

    # Posiciona o queijo em uma sala aleatória (rejeita paredes)
    while True:
        i = int(random.uniform(0, 2 * m))
        j = int(random.uniform(0, 2 * m))
        if maze[i][j] == room:
            maze[i][j] = cheese
            break

    return maze


def print_maze(maze):
    """Imprime o labirinto no terminal, uma linha por vez.

    Parameters
    ----------
    maze : list[list]
        Matriz retornada por :func:`generate_maze`.
    """
    print("\033[H\033[J")
    for row in maze:
        print(" ".join(map(str, row)))
    sleep(0.05)


def print_maze(maze):
    screen = "\n".join(" ".join(map(str, row)) for row in maze)
    print("\033[H\033[J" + "\n"*30 + screen, end="")
    sleep(0.003)


def find_path(maze, room=0, wall=1, path=2, cheese='.'):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    m, n = len(maze), len(maze[0])

    # Inicia a busca na posição start
    start = (1, 1)
    temp_stack = [(*start, directions)]
    stack_visiteds = [[]]

    while temp_stack:
        x, y, _directions = temp_stack.pop()
        if maze[x][y] == cheese:
            break
        stack_visiteds[-1].append((x, y))

        has_option = False
        for direction in _directions:
            dx, dy = direction
            nx, ny = x + dx, y + dy
            if 0 < nx < m and 0 < ny < n and maze[nx][ny] != wall:
                inverted_direction = (-direction[0], -direction[1])
                temp_stack.append((nx, ny, [d for d in directions if d != inverted_direction]))
                if has_option:
                    stack_visiteds.append([])
                has_option = True
        if not has_option:
            stack_visiteds.pop()
    final_path = [item for stack in stack_visiteds for item in stack]
    for x, y in final_path:
        maze[x][y] = path
        print_maze(maze)
    return final_path


# Example usage:
if __name__ == '__main__':
    while True:
        m, n = 10, 14  # Grid size
        m, n = 16, 28  # Grid size
        # random.seed(10110)
        maze = generate_maze(m, n, room="⬜", wall="🟥", cheese="🧀")
        print('Maze 1')
        print_maze(maze)
        find_path(maze, room="⬜", wall="🟥", path="🟩", cheese="🧀")
        sleep(0.5)
        maze_ = [["⬛" if i != "🟩" else i for i in line] for line in maze]
        print_maze(maze_)
        sleep(2)
