"""Seus testes do Marco 1 (veja a seção 6 do ENUNCIADO_MARCO1.md).

Regras: pelo menos 8 testes seus (o exemplo abaixo não conta), uma docstring em cada teste
dizendo qual caso ele cobre, e floats comparados com assertAlmostEqual ou np.allclose.
"""
import unittest

import numpy as np

from elevatoria.dados import por_tag
from elevatoria.serie import SerieTemporal


class TestPorTagExemplo(unittest.TestCase):
    """Exemplo do formato. `por_tag` é código existente da base."""

    def test_lista_vazia(self):
        """Sem registros, por_tag devolve uma lista vazia."""
        self.assertEqual(por_tag([], "PT101"), [])


# Acrescente abaixo as suas classes de teste, começando pelos testes de regressão da
# issue #4 (escreva-os ANTES de corrigir o defeito e confirme que falham).
class TestSerieTemporal(unittest.TestCase):
    """Classe de testes do módulo SerieTemporal, de serie.py"""

    def test_media_movel(self):
        """Verifica o tamanho e os valores da média móvel de três pontos."""
        s = SerieTemporal.de_lista(list(range(50)))
        mm = s.media_movel(3)
        self.assertEqual(len(mm), 48)
        self.assertTrue(np.allclose(mm, np.arange(1, 49)))


if __name__ == "__main__":
    unittest.main()
