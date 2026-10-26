"""Seus testes do Marco 1 (veja a seção 6 do ENUNCIADO_MARCO1.md).

Regras: pelo menos 8 testes seus (o exemplo abaixo não conta), uma docstring em cada teste
dizendo qual caso ele cobre, e floats comparados com assertAlmostEqual ou np.allclose.
"""
import unittest
from datetime import datetime

import numpy as np

from elevatoria.dados import ler_log, por_tag
from elevatoria.serie import SerieTemporal


class TestPorTagExemplo(unittest.TestCase):
    """Exemplo do formato. `por_tag` é código existente da base."""

    def test_lista_vazia(self):
        """Sem registros, por_tag devolve uma lista vazia."""
        self.assertEqual(por_tag([], "PT101"), [])


# Acrescente abaixo as suas classes de teste, começando pelos testes de regressão da
# issue #4 (escreva-os ANTES de corrigir o defeito e confirme que falham).
class TestSerieTemporal(unittest.TestCase):
    """Testes de regressão e contrato de SerieTemporal."""

    def test_media_movel(self):
        """Verifica o tamanho e os valores da média móvel de três pontos."""
        s = SerieTemporal.de_lista(list(range(50)))
        mm = s.media_movel(3)
        self.assertEqual(len(mm), 48)
        self.assertTrue(np.allclose(mm, np.arange(1, 49)))

    def test_media_movel_600_pontos_janela_30(self):
        """test_media_movel com um array de 600 pontos e janela de 30."""
        s = SerieTemporal.de_lista(np.arange(600))
        medias = s.media_movel(30)
        self.assertEqual(len(medias), 571)
        self.assertAlmostEqual(float(medias[0]), 14.5)
        self.assertAlmostEqual(float(medias[-1]), 584.5)

    def test_media_movel_janela_do_tamanho_da_serie(self):
        """Uma janela do tamanho da série produz exatamente uma média."""
        s = SerieTemporal.de_lista([1, 2, 3])
        medias = s.media_movel(3)
        self.assertEqual(len(medias), 1)
        self.assertAlmostEqual(float(medias[0]), 2.0)

    def test_media_movel_rejeita_janela_invalida(self):
        """Uma janela zero ou maior que a série levanta ValueError."""
        s = SerieTemporal.de_lista([1, 2, 3])
        for janela in [0, 4]:
            with self.subTest(janela=janela), self.assertRaises(ValueError):
                s.media_movel(janela)


class TestSerieTemporalReamostrar(unittest.TestCase):
    """Testes da reamostragem por blocos de SerieTemporal."""

    def test_reamostrar_calcula_medias_por_bloco(self):
        """Cada bloco completo é substituído pela sua média."""
        s = SerieTemporal.de_lista([1, 2, 3, 4, 5, 6])
        resultado = s.reamostrar(2)
        self.assertIsInstance(resultado, SerieTemporal)
        self.assertTrue(np.allclose(resultado, [1.5, 3.5, 5.5]))

    def test_reamostrar_descarta_sobra_no_fim(self):
        """Os pontos finais que não completam um bloco são descartados."""
        s = SerieTemporal.de_lista([1, 2, 3, 4, 5, 6, 7])
        resultado = s.reamostrar(3)
        self.assertEqual(len(resultado), 2)
        self.assertTrue(np.allclose(resultado, [2.0, 5.0]))


class TestLerLog(unittest.TestCase):
    """Testes das regras do contrato de ler_log em dados."""

    def test_texto_vazio(self):
        """Texto vazio retorna listas vazias."""
        registros, invalidas = ler_log("")
        self.assertEqual(registros, [])
        self.assertEqual(invalidas, [])

    def test_linhas_vazias_sao_ignoradas(self):
        """Linhas vazias ou só com espaços não são registros nem linhas inválidas."""
        registros, invalidas = ler_log("\n   \n\t\n")
        self.assertEqual(registros, [])
        self.assertEqual(invalidas, [])
        texto = "\n   \n2026-10-05 08:00:00 INFO PT102 contagens=10\n \t\n"
        registros, invalidas = ler_log(texto)
        self.assertEqual(len(registros), 1)
        self.assertEqual(invalidas, [])

    def test_data_impossivel_preserva_linha_como_invalida(self):
        """Uma data impossível faz a linha original aparecer entre as inválidas."""
        linha = "2026-13-05 08:00:00 INFO PT102 contagens=10"
        registros, invalidas = ler_log(linha)
        self.assertEqual(registros, [])
        self.assertEqual(invalidas, [linha])

    def test_preserva_ordem_dos_registros(self):
        """Os registros válidos mantêm a ordem das linhas de entrada."""
        texto = "\n".join([
            "2026-10-20 12:30:00 INFO PT101 valor=10",
            "2026-10-20 12:31:00 WARN PT102 valor=20",
            "2026-10-20 12:32:00 ALARME PT103 evento=falha"
        ])

        registros, invalidas = ler_log(texto)
        self.assertEqual([r.tag for r in registros], ["PT101", "PT102", "PT103"])
        self.assertEqual(invalidas, [])

    def test_linha_com_formato_invalido(self):
        """Uma linha que não corresponde ao padrão é descartada."""
        linha = "isto não é uma linha válida do log"
        registros, invalidas = ler_log(linha)
        self.assertEqual(registros, [])
        self.assertEqual(invalidas, [linha])

    def test_data_ou_hora_impossivel(self):
        """Datas e horas impossíveis tornam as linhas inválidas."""
        linhas = "\n".join([
            "2026-13-20 12:30:00 INFO PT102 contagens=10",
            "2026-10-20 25:30:00 INFO PT102 contagens=10",
        ])
        registros, invalidas = ler_log(linhas)
        self.assertEqual(registros, [])
        self.assertEqual(invalidas, linhas.splitlines())

    def test_linha_invalida_preserva_texto_original(self):
        """As linhas inválidas são devolvidas exatamente como recebidas."""
        linha = " linha com formato inválido  "
        registros, invalidas = ler_log(linha)
        self.assertEqual(registros, [])
        self.assertEqual(invalidas, [linha])


if __name__ == "__main__":
    unittest.main()
