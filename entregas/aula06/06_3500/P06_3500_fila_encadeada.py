from P06_3500_pilha_encadeada import PilhaEncadeada
from typing import Any


class FilaEncadeada():
    """Implementação de classe FilaEncadeada por composição da PilhaEncadeada"""

    def __init__(self):
        self._input_stack = PilhaEncadeada()
        self._output_stack = PilhaEncadeada()

    def queue(self, elem) -> None:
        """
        Adiciona um elemento no final da fila.

        Args:
            elem (Any): Elemento a ser adicionado.

        Complexity:
            O(1).
        """
        self._input_stack.push(elem)

    # Alias
    enfileirar = queue

    def dequeue(self) -> Any:
        """
        Remove e retorna o elemento que está no início da fila.

        Returns:
            Any: Elemento que está no início da fila.

        Raises:
            IndexError: Se a fila estiver vazia.

        Complexity:
            Average: O(1).
            Worst case: O(n).
        """
        if self._output_stack.is_empty():
            while not self._input_stack.is_empty():
                self._output_stack.push(self._input_stack.pop())
        return self._output_stack.pop()

    # Alias
    desenfileirar = dequeue

    def peek(self) -> Any:
        """
        Retorna o elemento que está no início da fila.

        Returns:
            Any: Elemento removido do início da fila.

        Raises:
            IndexError: Se a fila estiver vazia.

        Complexity:
            Averrage: O(1).
            Worst case: O(n).
        """
        if self._output_stack.is_empty():
            while not self._input_stack.is_empty():
                self._output_stack.push(self._input_stack.pop())
        return self._output_stack.top()

    # Alias
    frente = peek

    def is_empty(self) -> bool:
        """
        Verifica se a fila está vazia.

        Returns:
            bool: True caso não haja elementos na fila, caso contrário False.

        Complexity:
            O(1).
        """
        return not bool(self.size)

    # Alias
    esta_vazia = is_empty

    def len(self) -> int:
        """
        Retorna o número de elementos na fila.

        Returns:
            int: Número de elementos na fila.

        Complexity:
            O(1).
        """
        return self.size

    @property
    def size(self) -> int:
        """
        Retorna o número de elementos na fila.

        Returns:
            int: Número de elementos na fila.

        Complexity:
            O(1).
        """
        return len(self._input_stack) + len(self._output_stack)

    def __len__(self) -> int:
        """
        Retorna o número de elementos na fila.

        Returns:
            int: Número de elementos na fila.

        Complexity:
            O(1).
        """
        return self.size

    def __repr__(self) -> str:
        """
        Retorna uma representação textual da pilha (do topo para o começo). (percorre a lista algumas vezes)

        Complexity:
            O(n).
        """
        list_text = []
        len_output_stack = len(self._output_stack)
        len_input_stack = len(self._input_stack)

        # Transfere todos os itens de input_stack para output_stack
        while not self._input_stack.is_empty():
            list_text.append(str(self._input_stack.top()))
            self._output_stack.push(self._input_stack.pop())

        # Transfere todos os itens para input_stack
        while not self._output_stack.is_empty():
            self._input_stack.push(self._output_stack.pop())

        # Transfere os itens de output_stack para input_stack
        # Volta as listas para a configuração inicial
        while len_output_stack:
            len_output_stack -= 1
            list_text.append(str(self._input_stack.top()))
            self._output_stack.push(self._input_stack.pop())
        return " -> ".join(list_text)
