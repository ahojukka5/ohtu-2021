import unittest
from statistics import Statistics
from player import Player

players = [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri", "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89),
        ]


class PlayerReaderStub:
    def get_players(self):
        return players


class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(PlayerReaderStub())

    def test_sort_by_points(self):
        from statistics import sort_by_points
        self.assertEqual(sort_by_points(players[0]), 4+12)

    def test_search(self):
        player = self.statistics.search("Semenko")
        self.assertEqual(player, players[0])

    def test_search_not_found(self):
        player = self.statistics.search("notfound")
        self.assertIsNone(player)

    def test_team(self):
        team = self.statistics.team("EDM")
        self.assertEqual(len(team), 3)

    def test_top_scorers(self):
        best = self.statistics.top_scorers(1)
        self.assertEqual(best[0], players[-1])
