import unittest
from unittest.mock import Mock, ANY
from kassapaate import Kassapaate, HINTA
from maksukortti import Maksukortti


class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()

    def test_kortilta_velotetaan_hinta_jos_rahaa_on(self):
        maksukortti_mock = Mock()
        maksukortti_mock.saldo = 10

        self.kassa.osta_lounas(maksukortti_mock)

        maksukortti_mock.osta.assert_called_with(HINTA)

    def test_kortilta_ei_veloteta_jos_raha_ei_riita(self):
        maksukortti_mock = Mock()
        maksukortti_mock.saldo = 4

        self.kassa.osta_lounas(maksukortti_mock)

        maksukortti_mock.osta.assert_not_called()

    def test_lataa_positiivinen_summa(self):
        maksukortti_mock = Mock()
        self.kassa.lataa(maksukortti_mock, 5)
        maksukortti_mock.lataa.assert_called()

    def test_lataa_negatiivinen_summa(self):
        maksukortti_mock = Mock()
        self.kassa.lataa(maksukortti_mock, -5)
        maksukortti_mock.lataa.assert_not_called()
