class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.nation = dict['nationality']
        self.team = dict['team']
        self.games = dict['games']
        self.goals = dict['goals']
        self.assists = dict['assists']
        self.points = self.goals + self.assists
    
    def __str__(self):
        return f"{self.name:20} {self.team:15} {self.goals} + {self.assists} = {self.goals + self.assists}"
