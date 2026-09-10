import random
from unittest import TestCase, main

from P06_3500_fila_encadeada import FilaEncadeada
from P06_3500_pilha_encadeada import PilhaEncadeada


class TestPilhaEncadeada(TestCase):
    """
    Testes obrigatórios (unittest) para a pilha:
        Ordem LIFO em sequência de push/pop;
        Pop e topo em pilha vazia;
        Coerência de len após inserções e remoções;
        Alternância de operações;
        Armazenamento de itens de tipos diferentes, incluindo valores repetidos e None.
    """

    def test_lifo(self):
        """
        Teste de ordem LIFO em sequencia de push/pop.

        Adiciona três elementos em uma PilhaEncadeada vazia, depois remove os elementos.
        Verifica as operações top e pop.
        """
        stack = PilhaEncadeada()
        stack.push("A")
        stack.push("B")
        stack.push("C")

        self.assertEqual(stack.top(), 'C')
        self.assertEqual(stack.pop(), 'C')

        self.assertEqual(stack.top(), 'B')
        self.assertEqual(stack.pop(), 'B')

        self.assertEqual(stack.top(), 'A')
        self.assertEqual(stack.pop(), 'A')

    def test_pop_and_top_in_empty_stack(self):
        """
        Teste de pop e top em PilhaEncadeada vazia.

        Verifica se a pilha encadeada retorna corretamente exceção IndexError durante
        as operações top e pop com a pilha vazia.
        """
        stack = PilhaEncadeada()
        self.assertRaises(IndexError, stack.pop)
        self.assertRaises(IndexError, stack.top)

    def test_len(self):
        """
        Teste de coerência de len após inserções e remoções.

        Adiciona 1000 elementos e os remove, enquanto faz verificações de __len__.
        """

        stack = PilhaEncadeada()

        # Testes adicionando elementos
        for c in range(1, 1001):
            stack.push(1)
            self.assertEqual(len(stack), c)

        # Testes removendo elementos
        for c in range(1, 1001):
            stack.pop()
            self.assertEqual(len(stack), 1000-c)

    def test_alternating_operations(self):
        """
        Teste de alternância de operações.

        Adiciona ou remove elementos em uma pilha de maneira imprevisível, fazendo verificações dos métodos:
            push, pop, top, len.
        """
        stack = PilhaEncadeada()
        size_stack = 0

        for _ in range(10000):
            operation = random.choice(["push", "pop", "top", "len"])

            if operation == "push":
                size_stack += 1
                stack.push(str(size_stack))
                continue

            if operation == "pop":
                if not size_stack:
                    continue
                self.assertEqual(stack.pop(), str(size_stack))
                size_stack -= 1
                continue

            if operation == "top":
                if not size_stack:
                    continue
                self.assertEqual(stack.top(), str(size_stack))
                continue

            if operation == "len":
                self.assertEqual(len(stack), size_stack)

    def test_storage_of_different_types(self):
        """
        Testa o armazenamento de itens de tipos diferentes, incluindo valores repetidos e None.
        """
        stack = PilhaEncadeada()
        elements = [None, "X", Exception]
        size = 0

        for elem in elements:
            for _ in range(100):
                size += 1
                stack.push(elem)
                self.assertEqual(stack.top(), elem)
                self.assertEqual(len(stack), size)

        for elem in elements[::-1]:
            for _ in range(100):
                size -= 1
                self.assertEqual(stack.pop(), elem)
                self.assertEqual(len(stack), size)


class TestFilaEncadeada(TestCase):
    """
    Testes obrigatórios (unittest) para a fila:
        ordem FIFO;
        intercalação de enfileirar e desenfileirar;
        esvaziar e voltar a usar a mesma instância;
        desenfileirar e frente em fila vazia; 
        coerência de len.
    """

    def test_fifo(self):
        """
        Teste de ordem FIFO em sequencia de enfileirar/desenfileirar.

        Adiciona três elementos em uma FilaEncadeada vazia, depois remove os elementos.
        Verifica as operações frente, enfileirar, desenfileirar.
        """
        queue = FilaEncadeada()
        queue.enfileirar("A")
        queue.enfileirar("B")
        queue.enfileirar("C")

        self.assertEqual(queue.frente(), 'A')
        self.assertEqual(queue.desenfileirar(), 'A')

        self.assertEqual(queue.frente(), 'B')
        self.assertEqual(queue.desenfileirar(), 'B')

        self.assertEqual(queue.frente(), 'C')
        self.assertEqual(queue.desenfileirar(), 'C')

    def test_alternating_operations(self):
        """
        Teste de alternância de operações.

        Adiciona ou remove elementos em uma fila de maneira imprevisível, fazendo verificações dos métodos:
            enfileirar, desenfileirar, frente, len.
        """
        queue = FilaEncadeada()
        added_queue = 0
        removed_queue = 0

        for _ in range(10000):
            operation = random.choice(["enfileirar", "desenfileirar", "frente", "len"])

            if operation == "enfileirar":
                added_queue += 1
                queue.enfileirar(str(added_queue))
                continue

            if operation == "desenfileirar":
                if not added_queue-removed_queue:
                    continue
                self.assertEqual(queue.desenfileirar(), str(removed_queue+1))
                removed_queue += 1
                continue

            if operation == "frente":
                if not added_queue-removed_queue:
                    continue
                self.assertEqual(queue.frente(), str(removed_queue+1))
                continue

            if operation == "len":
                self.assertEqual(len(queue), added_queue-removed_queue)

    def test_empty_and_reuse_the_same_instance(self):
        """
        Teste esvaziar e voltar a usar a mesma instância

        Adiciona e remove todos os elementos diversas vezes.
        """

        queue = FilaEncadeada()
        for _ in range(40):
            for _ in range(100):
                queue.enfileirar(1)
            for i in range(100):
                self.assertEqual(len(queue), 100-i)
                self.assertEqual(queue.desenfileirar(), 1)

    def test_dequeue_and_peek_in_empty_queue(self):
        """
        Teste de desenfileirar e frente em FilaEncadeada vazia.

        Verifica se a fila encadeada retorna corretamente exceção IndexError durante
        as operações desenfileirar e frente com a fila vazia.
        """
        queue = FilaEncadeada()
        self.assertRaises(IndexError, queue.desenfileirar)
        self.assertRaises(IndexError, queue.frente)

    def test_len(self):
        """
        Teste de coerência de len após inserções e remoções.

        Adiciona 1000 elementos e os remove, enquanto faz verificações de __len__.
        """

        queue = FilaEncadeada()

        # Testes adicionando elementos
        for c in range(1, 1001):
            queue.enfileirar(1)
            self.assertEqual(len(queue), c)

        # Testes removendo elementos
        for c in range(1, 1001):
            queue.desenfileirar()
            self.assertEqual(len(queue), 1000-c)


if __name__ == '__main__':
    # main(verbosity=2)
    main()
