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

    def test_haettu_pelaaja_loytyy(self):
        self.assertEqual(self.stats.search("Gretzky"), self.stats._players[4])

    def test_haettua_pelaajaa_ei_ole(self):
        self.assertIsNone(self.stats.search("Bretzky"))

    def test_tiimin_hakeminen_onnistuu(self):
        result = [self.stats._players[0], self.stats._players[2], self.stats._players[4]]
        self.assertEqual(self.stats.team("EDM"), result)

    def test_top3_hakeminen_pisteilla_onnistuu(self):
        result = [self.stats._players[4], self.stats._players[1], self.stats._players[3]]
        self.assertEqual(self.stats.top(2), result)

    def test_top3_hakeminen_maaleilla_onnistuu(self):
        result = [self.stats._players[1], self.stats._players[3], self.stats._players[2]]
        self.assertEqual(self.stats.top(2, SortBy.GOALS), result)

    def test_top3_hakeminen_syotoilla_onnistuu(self):
        result = [self.stats._players[4], self.stats._players[3], self.stats._players[1]]
        self.assertEqual(self.stats.top(2, SortBy.ASSISTS), result)
