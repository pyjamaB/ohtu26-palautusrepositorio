import unittest
from unittest.mock import Mock
from kauppa import Kauppa
from tuote import Tuote
from viitegeneraattori import Viitegeneraattori

class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock(wraps=Viitegeneraattori())
        self.varasto_mock = Mock()

        tuotteet = {
            1: Tuote(1, "maito", 5),
            2: Tuote(2, "sokeri", 7)
        }
        saldot = {
            1: 10,
            2: 8
        }
        self.varasto_mock.saldo.side_effect = saldot.get
        self.varasto_mock.hae_tuote.side_effect = tuotteet.get

        self.kauppa = Kauppa(
            self.varasto_mock,
            self.pankki_mock,
            self.viitegeneraattori_mock
        )
        self.kauppa.aloita_asiointi()

    def test_maksettaessa_ostos_pankin_metodia_tilisiirto_kutsutaan(self):
        # tehdään ostokset
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_maksettaessa_ostos_pankin_metodia_tilisiirto_kutsutaan_oikealla_asiakkaalla_tilinumeroilla_summalla(self):
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", 2, "12345", "33333-44455", 5
        )

    def test_maksettaessa_kaksi_eri_tuotetta_pankin_metodia_tilisiirto_kutsutaan_oikealla_asiakkaalla_tilinumeroilla_summalla(self):
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", 2, "12345", "33333-44455", 12
        )

    def test_maksettaessa_kaksi_samaa_varastossa_olevaa_tuotetta_pankin_metodia_tilisiirto_kutsutaan_oikealla_asiakkaalla_tilinumeroilla_summalla(self):
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", 2, "12345", "33333-44455", 10
        )

    def test_maksettaessa_kaksi_eri_tuotetta_toinen_loppu_pankin_metodia_tilisiirto_kutsutaan_oikealla_asiakkaalla_tilinumeroilla_summalla(self):
        self.varasto_mock.saldo.side_effect = {1: 10, 2: 0}.get
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", 2, "12345", "33333-44455", 5
        )

    def test_aloita_asionti_nollaa_edellisen_ostoksen_tiedot(self):
        self.kauppa.lisaa_koriin(1)
        self.kauppa.aloita_asiointi()
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", 2, "12345", "33333-44455", 0)

    def test_kauppa_pyytaa_uuden_viitenumeron_jokaiselle_maksutapahtumalle(self):
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", 3, "12345", "33333-44455", 5)

    def test_tuote_poistuu_ostoskorista_poistettaessa(self):
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.poista_korista(1)

        self.kauppa.tilimaksu("pekka", "12345")
        
        self.pankki_mock.tilisiirto.assert_called_with("pekka", 2, "12345", "33333-44455", 7)