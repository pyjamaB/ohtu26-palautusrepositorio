import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),  #  4+12 = 16
            Player("Lemieux", "PIT", 45, 54), # 45+54 = 99
            Player("Kurri",   "EDM", 37, 53), # 37+53 = 90
            Player("Yzerman", "DET", 42, 56), # 42+56 = 98
            Player("Gretzky", "EDM", 35, 89)  # 35+89 = 124
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )
    def test_luokka_luo_pelaajalistan(self):
        self.assertEqual(len(self.stats._players), 5)
        self.assertEqual(str(self.stats._players[0]), "Semenko EDM 4 + 12 = 16")

    def test_etsinta_loytaa_pelaajan(self):
        tulos = self.stats.search("Lemieux")
        self.assertEqual(tulos.name, "Lemieux")

    def test_etsinta_palauttaa_none(self):
        tulos = self.stats.search("Selanne")
        self.assertEqual(tulos, None)

    def test_joukkueen_pelaajat_haetaan_oikein(self):
        joukkue = self.stats.team("DET")
        self.assertEqual(joukkue[0].name, "Yzerman")

    def test_parhaat_pelaajat_palautetaan_oikein(self):
        parhaat = self.stats.top(4)
        self.assertEqual(parhaat[0].name, "Gretzky")

    def test_parhaat_pelaajat_palautetaan_oikein_pisteet(self):
        parhaat = self.stats.top(4, SortBy.POINTS)
        self.assertEqual(parhaat[0].name, "Gretzky")

    def test_parhaat_pelaajat_palautetaan_oikein_maalit(self):
        parhaat = self.stats.top(4, SortBy.GOALS)
        self.assertEqual(parhaat[0].name, "Lemieux")

    def test_parhaat_pelaajat_palautetaan_oikein_syotot(self):
        parhaat = self.stats.top(4, SortBy.ASSISTS)
        self.assertEqual(parhaat[0].name, "Gretzky")