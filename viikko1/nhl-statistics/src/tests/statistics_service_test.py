import unittest
from statistics_service import StatisticsService
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

    def test_konstruktori_luo_pelaajatiedot_oikein(self):
        players = [str(player) for player in self.stats._players]
        real_players = [
            "Semenko EDM 4 + 12 = 16",
            "Lemieux PIT 45 + 54 = 99",
            "Kurri EDM 37 + 53 = 90",
            "Yzerman DET 42 + 56 = 98",
            "Gretzky EDM 35 + 89 = 124"
        ]

        self.assertEqual(players, real_players)

    def test_haettu_pelaaja_loytyy(self):
        result = None
        for player in self.stats._players:
            if "Gretzky" in player.name:
                result = player

        real_result = self.stats._players[4]

        self.assertEqual(result, real_result)

    def test_haettua_pelaajaa_ei_ole(self):
        result = None
        for player in self.stats._players:
            if "Bretzky" in player.name:
                result = player

        self.assertIsNone(result)

