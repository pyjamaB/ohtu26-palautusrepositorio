import requests
from player import Player

class PlayerReader: # pylint: disable=too-few-public-methods
    def __init__(self, osoite):
        self._url = osoite

    def get_players(self):
        with requests.get (self._url, timeout=10) as response:
            response.raise_for_status()
        data = response.json()
        players = []

        for player_dict in data:
            player = Player(player_dict)
            players.append(player)

        return players
