from rich.console import Console
from rich.table import Table
from player_reader import PlayerReader
from player_stats import PlayerStats

console = Console()



def main():

    print("[bold magenta] Select season and nationality. Exit by writing exit [/bold magenta]")
    season = input("Season[2018-19/2019-20/2020-21/2021-22/2022-23/2023-24/2024-25/2025-26]:")
    if season == "exit":
        return
    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    while True:
        nationality = input("Nationality:")

        if nationality == "exit":
            break
        reader = PlayerReader(url)
        stats = PlayerStats(reader)
        print(f"Season {season} players from {nationality}")
        players = stats.top_scorers_by_nationality(nationality)
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
                str(player.points))

        console.print(table)


if __name__ == "__main__":
    main()
