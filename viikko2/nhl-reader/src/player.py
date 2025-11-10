import requests

class Player:
    def __init__(self, dict_in_question):
        self.name = dict_in_question['name']
        self.nationality = dict_in_question['nationality']
        self.teams = dict_in_question['team']
        self.games = dict_in_question['games']
        self.goals = dict_in_question['goals']
        self.assists = dict_in_question['assists']
        self.points = self.goals + self.assists

    def extra_method_for_player_name(self):
        return f"Player: {self.name}"

    def __str__(self):
        return f"{self.name:20} {self.teams:15} {self.goals} + {self.assists} = {self.points}"


class PlayerReader:
    def __init__(self, url):
        self.all_players = requests.get(url, timeout=60).json()
        self.players = []

    def extra_method_for_fun(self):
        return self.all_players

    def get_players(self):
        players = []
        for player_dict in self.all_players:
            player = Player(player_dict)
            players.append(player)

        return players


class PlayerStats:
    def __init__(self, reader):
        self.players = reader.get_players()

    def extra_extra_method_for_fun(self):
        return self.players

    def top_scorers_by_nationality(self, nationality):
        self.players.sort(key=lambda player: player.points)

        result = []

        for player in reversed(self.players):
            if player.nationality == nationality:
                info = [player.name, player.teams, player.goals, player.assists, player.points]
                result.append(info)

        return result
