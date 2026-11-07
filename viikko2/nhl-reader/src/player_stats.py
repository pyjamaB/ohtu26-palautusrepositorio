
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

    def top_goal_scorers(self, how_many):
        """Palauttaa how_many eniten maaleja 
        tehnyttä pelaajaa maalimäärän mukaan laskevassa järjestyksessä"""
        sorted_players = sorted(self._players, key=lambda x: x.goals, reverse=True)
        return sorted_players[:how_many]

    def top_scorers_by_team(self, team):
        team_players = [
            player for player in self._players
            if team in player.team.split(", ")
        ]

        return sorted(
            team_players,
            key=lambda player: player.points,
            reverse=True)
