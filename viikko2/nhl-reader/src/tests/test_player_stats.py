import unittest

from player import Player
from player_stats import PlayerStats


class PlayerReaderStub:
    def __init__(self, players):
        self._players = players

    def get_players(self):
        return self._players


class TestPlayerStats(unittest.TestCase):
    def setUp(self):
        players = [
            Player({
                "name": "Finnish Player",
                "team": "FIN",
                "nationality": "FIN",
                "goals": 10,
                "assists": 20,
            }),
            Player({
                "name": "Canadian Player",
                "team": "CAN",
                "nationality": "CAN",
                "goals": 20,
                "assists": 10,
            }),
            Player({
                "name": "Another Finnish Player",
                "team": "FIN",
                "nationality": "FIN",
                "goals": 5,
                "assists": 5,
            }),
        ]
        self.stats = PlayerStats(PlayerReaderStub(players))

    def test_top_scorers_by_nationality_returns_players_in_points_order(self):
        players = self.stats.top_scorers_by_nationality("FIN")

        self.assertEqual(
            [player.name for player in players],
            ["Finnish Player", "Another Finnish Player"],
        )

    def test_top_scorers_by_team_returns_players_in_points_order(self):
        players = self.stats.top_scorers_by_team("FIN")

        self.assertEqual(
            [player.name for player in players],
            ["Finnish Player", "Another Finnish Player"],
        )

    def test_top_goal_scorers_returns_requested_number_of_players(self):
        players = self.stats.top_goal_scorers(2)

        self.assertEqual(
            [player.name for player in players],
            ["Canadian Player", "Finnish Player"],
        )
