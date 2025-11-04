class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.nation = dict['nationality']
        self.team = dict['team']
        self.games = dict['games']
    
    def __str__(self):
        return f"{self.name}, {self.nation}, {self.team}, {self.games}"
