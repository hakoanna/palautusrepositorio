import requests

class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.nationality = dict['nationality']
        self.teams = dict['team']
        self.games = dict['games']
        self.goals = dict['goals']
        self.assists = dict['assists']
        self.points = self.goals + self.assists
    
    def __str__(self):
        return f"{self.name:20} {self.teams:15} {self.goals} + {self.assists} = {self.goals + self.assists}"
    

class PlayerReader:
    def __init__(self, url):
        self.all_players = requests.get(url).json()

    def get_players(self):
        self.players = []
        for player_dict in self.all_players:
            player = Player(player_dict)
            self.players.append(player)

        return self.players


class PlayerStats:
    def __init__(self, reader):
        self.players = reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        self.players.sort(key=lambda player: player.points)

        result = []
    
        for player in reversed(self.players):
            if player.nationality == nationality:
                result.append([player.name, player.teams, player.goals, player.assists, player.points])

        return result
