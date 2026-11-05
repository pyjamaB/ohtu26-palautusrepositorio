
class PlayerStats:
    def __init__(self, pelaajat):
        reader = pelaajat

        self._players = reader.get_players()

    def top_scorers_by_nationality(self, nationality):

        players = self._players

        top_scorers = []
        for player in players:
            if player.nationality == nationality:
                top_scorers.append(player)

        sorted_team = sorted(top_scorers, key=lambda x: x.points, reverse=True)
        return sorted_team
