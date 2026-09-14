from typing import Any

class PilhaEncadeada:
    """Estrutura de dados PilhaEncadeada."""

    class _No:
        """Classe interna _No da PilhaEncadeada."""

        def __init__(self, val, previous) -> None:
            """
            Armazena o valor e a referência para o elemento anterior.

            Args:
                val (Any): Elemento a ser armazenado.
                previous (_No): Referência para o elemento anterior.

            Complexity:
                O(1).
            """

            self.val = val
            self.previous = previous

    def __init__(self):
        """
        Inicializa uma PilhaEncadeada vazia.

        Complexity:
            O(1).
        """
        self._head = None  # Último nó da PilhaEncadeada. (Topo)
        self._size = 0  # Quantidade de elementos na PilhaEncadeada.

    def push(self, elem) -> None:
        """
        Adiciona um elemento no topo da pilha.

        Args:
            elem (Any): Elemento a ser adicionado.

        Complexity:
            O(1).
        """
        no = self._No(elem, self._head)
        self._head = no
        self._size += 1

    def pop(self) -> Any:
        """
        Remove e retorna o elemento do topo da pilha.

        Returns:
            Any: Elemento removido do topo da pilha.

        Raises:
            IndexError: Se não houver elementos na pilha.

        Complexity:
            O(1).
        """
        if not self._size:
            raise IndexError("A pilha está vazia")

        self._size -= 1
        self._head, elem = self._head.previous, self._head.val
        return elem

    def top(self) -> Any:
        """
        Retorna o elemento do topo da pilha.

        Returns:
            Any: O elemento do topo da pilha.

        Raises:
            IndexError: Se não houver elementos na pilha.

        Complexity:
            O(1).
        """
        if not self._size:
            raise IndexError("A pilha está vazia")
        return self._head.val

    # Alias
    topo = top

    def is_empty(self) -> bool:
        """
        Verifica se a pilha está vazia.

        Returns:
            bool: True caso não haja elementos na pilha, caso contrário False.

        Complexity:
            O(1).
        """
        return not bool(self._size)

    # Alias
    esta_vazia = is_empty

    def len(self) -> int:
        """
        Retorna o número de elementos na pilha.

        Returns:
            int: Número de elementos na pilha.

        Complexity:
            O(1).
        """
        return self._size

    def __len__(self) -> int:
        """
        Retorna o número de elementos na pilha.

        Returns:
            int: Número de elementos na pilha.

        Complexity:
            O(1).
        """
        return self.len()

    def __repr__(self) -> str:
        """
        Retorna uma representação textual da pilha.

        Complexity:
            O(n).
        """
        list_text = [f"{self._head.val}"]

        current = self._head
        while current.previous:
            current = current.previous
            list_text.append(f" -> {current.val}")
        return ''.join(list_text)


if __name__ == "__main__":
    stack = PilhaEncadeada()
    for i in range(1, 11):
        stack.push(i)

    print(stack)
    print("Size:", len(stack))
    print("Topo:", stack.topo())