class Player: # pylint: disable=too-few-public-methods
    def __init__(self, player_dict):
        self.name = player_dict['name']
        self.team = player_dict['team']
        self.nationality = player_dict['nationality']
        self.goals = player_dict['goals']
        self.assists = player_dict['assists']
        self.points = int(self.goals) + int(self.assists)

    def __str__(self):
        return f"""{self.name:<20} {self.team:<15}
        {self.goals:<3} + {self.assists:<3} = {self.points:<3}"""
