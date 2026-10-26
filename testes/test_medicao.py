"""Seus testes do Marco 2 (veja a seção 5 do ENUNCIADO_MARCO2.md).

Regras: pelo menos 4 testes seus (o exemplo abaixo não conta), uma docstring em cada teste
dizendo qual caso ele cobre, e floats comparados com assertAlmostEqual, math.isclose ou
np.allclose, a não ser que a igualdade exata seja justamente o que você quer testar.
"""
import unittest
from datetime import datetime

from elevatoria.acumuladores import AcumuladorIngenuo, AcumuladorKahan
from elevatoria.calibracao import CurvaCalibracao
from elevatoria.dados import Registro
from elevatoria.medicao import medir


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

    def test_parcelas_pequenas_nao_se_perdem(self):
        """Soma de 1,0 com 10.000 parcelas de 1e-16, que a soma ingênua perde."""
        acumulador = AcumuladorKahan()
        acumulador.adicionar_todos([1.0] + [1e-16] * 10_000)
        self.assertAlmostEqual(acumulador.total, 1.000000000001, delta=1e-15)

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


class TestMedir(unittest.TestCase):
    """Testes da função medir, de elevatoria.medicao."""

    def test_medir_com_u_sistematica_negativa(self):
        """ValueError para u_sistematica negativa."""

        contagens = [500.0, 501.0, 499.0, 502.0, 498.0, 503.0, 497.0, 504.0, 496.0, 505.0]
        registros = [
            Registro(instante=datetime(2026, 10, 26), nivel="INFO", tag="PT101", valores={"contagens": contagem})
            for contagem in contagens
        ]
        curva = CurvaCalibracao([0, 500, 1000], [0, 50, 100], metodo="linear")

        with self.assertRaises(ValueError):
            medir(registros, "PT101", curva, u_sistematica=-1.0)

    def test_medir_com_tag_com_menos_de_duas_leituras(self):
        """ValueError para tag com menos de duas leituras."""

        registros = [Registro(instante=datetime(2026, 10, 26), nivel="INFO", tag="PT101", valores={"contagens": 1000.0})]
        curva = CurvaCalibracao([0, 500, 1000], [0, 50, 100], metodo="linear")

        with self.assertRaises(ValueError):
            medir(registros, "PT101", curva)

    def test_medir_com_mad_zero(self):
        """ValueError para MAD = 0."""

        registros = [Registro(instante=datetime(2026, 10, 26), nivel="INFO", tag="PT101", valores={"contagens": 1000.0}) for _ in range(10)]
        curva = CurvaCalibracao([0, 500, 1000], [0, 50, 100], metodo="linear")

        with self.assertRaises(ValueError):
            medir(registros, "PT101", curva)

    def test_medir_com_menos_de_duas_leituras_validas(self):
        """ValueError quando sobra só uma leitura válida."""

        contagens = [100.0, 500.0, 900.0]
        registros = [
            Registro(instante=datetime(2026, 10, 26), nivel="INFO", tag="PT101", valores={"contagens": contagem})
            for contagem in contagens
        ]

        curva = CurvaCalibracao([0, 500, 1000], [0, 50, 100], metodo="linear")

        with self.assertRaises(ValueError):
            medir(registros, "PT101", curva, limiar=0.5)


if __name__ == "__main__":
    unittest.main()
