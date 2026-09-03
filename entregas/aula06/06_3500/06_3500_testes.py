from P06_3500_fila_encadeada import PilhaEncadeada
from unittest import TestCase, main
import random

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
            

if __name__ == '__main__':
    main(verbosity=2)