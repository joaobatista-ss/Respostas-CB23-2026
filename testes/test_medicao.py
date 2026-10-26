"""Seus testes do Marco 2 (veja a seção 5 do ENUNCIADO_MARCO2.md).

Regras: pelo menos 4 testes seus (o exemplo abaixo não conta), uma docstring em cada teste
dizendo qual caso ele cobre, e floats comparados com assertAlmostEqual, math.isclose ou
np.allclose, a não ser que a igualdade exata seja justamente o que você quer testar.
"""
import unittest

from elevatoria.acumuladores import AcumuladorIngenuo, AcumuladorKahan


class TestAcumuladorIngenuoExemplo(unittest.TestCase):
    """Exemplo do formato. `AcumuladorIngenuo` é código existente da base."""

    def test_sem_parcelas(self):
        """Sem nenhuma parcela, o total é zero."""
        self.assertEqual(AcumuladorIngenuo().total, 0.0)


# Acrescente abaixo as suas classes de teste, começando pelos testes de regressão da
# issue #7 (escreva-os ANTES de corrigir o defeito e confirme que falham).
class TestAcumuladorKahan(unittest.TestCase):
    """Testes do TestAcumuladorKahan"""

    def test_soma_float(self):
        """Soma de 1.000.000 de pulsos de 0,1 L cada."""
        acumulador = AcumuladorKahan()
        for _ in range(1_000_000):
            acumulador.adicionar(0.1)
        self.assertAlmostEqual(acumulador.total, 100_000.0)

    def test_soma_com_zeros(self):
        """Soma com parcelas zero."""
        acumulador = AcumuladorKahan()
        for _ in range(1_000):
            acumulador.adicionar(0.0)
        self.assertAlmostEqual(acumulador.total, 0.0)
        acumulador.adicionar(5.0)
        self.assertAlmostEqual(acumulador.total, 5.0)

    def test_soma_negativos(self):
        """Soma com parcelas negativas."""
        acumulador = AcumuladorKahan()
        acumulador.adicionar(-1.0)
        acumulador.adicionar(-2.0)
        self.assertAlmostEqual(acumulador.total, -3.0)

    def test_adicionar_todos(self):
        """Teste do método adicionar_todos."""
        acumulador = AcumuladorKahan()
        valores = [1.0, 2.0, 3.0]
        acumulador.adicionar_todos(valores)
        self.assertAlmostEqual(acumulador.total, 6.0)


if __name__ == "__main__":
    unittest.main()
