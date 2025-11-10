from rich.console import Console
from rich.table import Table
from player import PlayerReader, PlayerStats


def main():
    season = input("Season: ")
    nationality = input("Nationality: ")

    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality(nationality)
    console = Console()
    console.print(create_table(players, season, nationality))


def create_table(players, season, nationality):
    table = Table(title=f"Season {season} players from {nationality}")

    table.add_column("Player", style="cyan")
    table.add_column("Teams", style="magenta")
    table.add_column("Goals", style="green")
    table.add_column("Assists", style="green")
    table.add_column("Points", style="green")

    for player in players:
        table.add_row(str(player[0]), str(player[1]), str(player[2]), str(player[3]), str(player[4]))

    return table

if __name__ == '__main__':
    main()
