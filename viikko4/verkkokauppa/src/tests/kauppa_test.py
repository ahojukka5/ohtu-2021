import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote


class TestKauppa(unittest.TestCase):

    def setUp(self):
        self.pankki_mock = pankki_mock = Mock()
        viitegeneraattori_mock = Mock()

        # palautetaan aina arvo 42
        viitegeneraattori_mock.uusi.return_value = 42

        varasto_mock = Mock()

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id == 2:
                return 10
            if tuote_id == 3:
                return 0

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(2, "jauheliha", 10)
            if tuote_id == 3:
                return Tuote(3, "porkkana", 3)

        # otetaan toteutukset käyttöön
        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # alustetaan kauppa
        self.kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)

    def kauppareissu_0(self):

        kauppa = self.kauppa
        tilisiirto = self.pankki_mock.tilisiirto

        # tehdään ostokset
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_kauppareissu_1(self):
        """Aloitetaan asiointi, koriin lisätään tuote, jota varastossa on ja
        suoritetaan ostos, eli kutsutaan metodia kaupan tilimaksu, varmista että
        kutsutaan pankin metodia tilisiirto oikealla asiakkaalla, tilinumeroilla
        ja summalla."""

        kauppa = self.kauppa
        tilisiirto = self.pankki_mock.tilisiirto

        # tehdään ostokset
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        nimi = "pekka"
        viitenumero = 42
        tililta = "12345"
        tilille = ANY
        summa = 5
        tilisiirto.assert_called_with(nimi, viitenumero, tililta, tilille, summa)

    def test_kaupppareissu_2(self):
        """Aloitetaan asiointi, koriin lisätään kaksi eri tuotetta, joita
        varastossa on ja suoritetaan ostos, varmista että kutsutaan pankin
        metodia tilisiirto oikealla asiakkaalla, tilinumerolla ja summalla."""

        kauppa = self.kauppa
        tilisiirto = self.pankki_mock.tilisiirto

        # tehdään ostokset
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(2)
        kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        nimi = "pekka"
        viitenumero = 42
        tililta = "12345"
        tilille = ANY
        summa = 15
        tilisiirto.assert_called_with(nimi, viitenumero, tililta, tilille, summa)

    def test_kaupppareissu_3(self):
        """Aloitetaan asiointi, koriin lisätään kaksi samaa tuotetta, jota on
        varastossa tarpeeksi ja suoritetaan ostos, varmista että kutsutaan
        pankin metodia tilisiirto oikealla asiakkaalla, tilinumerolla ja
        summalla."""

        kauppa = self.kauppa
        tilisiirto = self.pankki_mock.tilisiirto

        # tehdään ostokset
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        nimi = "pekka"
        viitenumero = 42
        tililta = "12345"
        tilille = ANY
        summa = 10
        tilisiirto.assert_called_with(nimi, viitenumero, tililta, tilille, summa)

    def test_kaupppareissu_4(self):
        """Aloitetaan asiointi, koriin lisätään tuote, jota on varastossa
        tarpeeksi ja tuote joka on loppu ja suoritetaan ostos, varmista että
        kutsutaan pankin metodia tilisiirto oikealla asiakkaalla, tilinumerolla
        ja summalla."""

        kauppa = self.kauppa
        tilisiirto = self.pankki_mock.tilisiirto

        # tehdään ostokset
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(3)
        kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        nimi = "pekka"
        viitenumero = 42
        tililta = "12345"
        tilille = ANY
        summa = 5
        tilisiirto.assert_called_with(nimi, viitenumero, tililta, tilille, summa)
