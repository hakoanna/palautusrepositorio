from player import PlayerReader, PlayerStats


def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    reader = PlayerReader(url)
    print(reader)
    stats = PlayerStats(reader)
    print(stats)
    players = stats.top_scorers_by_nationality("FIN")

    for player in players:
        print(player)

if __name__ == '__main__':
    main()