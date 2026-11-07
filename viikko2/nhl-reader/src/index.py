from rich.console import Console
from rich.table import Table
from player_reader import PlayerReader
from player_stats import PlayerStats

console = Console()

def create_table(players):
    table = Table(title="")

    table.add_column("Released", justify="left", style="cyan", no_wrap=True)
    table.add_column("Teams", justify="left", style="magenta")
    table.add_column("Goals", justify="right", style="green")
    table.add_column("Assists", justify="right", style="magenta")
    table.add_column("Points", justify="right", style="green")

    for player in players:
        table.add_row(
            player.name,
            player.team,
            str(player.goals),
            str(player.assists),
            str(player.points)
        )

    return table

def show_players(url, nationality):
    reader = PlayerReader(url)
    stats = PlayerStats(reader)

    print(f"Season players from {nationality}")
    players = stats.top_scorers_by_nationality(nationality)

    console.print(create_table(players))

def show_team_players(url, team):
    reader = PlayerReader(url)
    stats = PlayerStats(reader)

    print(f"Team {team} players")
    players = stats.top_scorers_by_team(team)

    console.print(create_table(players))

def show_search_results(url, search_type, value):
    search_type = search_type.strip().lower()
    value = value.strip().upper()

    if search_type == "team":
        show_team_players(url, value)
    elif search_type == "nationality":
        show_players(url, value)
    else:
        print("Unknown search type.")


def search_players(url):
    while True:
        search_type = input(
            "Search by team or nationality? "
            "Enter 'team', 'nationality' or 'exit': ")

        if search_type == "exit":
            break

        value = input(f"Enter {search_type}: ")
        show_search_results(url, search_type, value)


def get_season_url():
    print("[bold magenta] Select season and nationality. Exit by writing exit [/bold magenta]")
    season = input(
        "Season[2018-19/2019-20/2020-21/2021-22/2022-23/"
        "2023-24/2024-25/2025-26]:"
    )
    if season == "exit":
        return None

    return f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"


def main():
    url = get_season_url()
    if url is not None:
        search_players(url)


if __name__ == "__main__":
    main()
