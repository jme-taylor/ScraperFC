import json

from ScraperFC.understat import Understat

understat = Understat()

print(understat.get_season_link("2023/2024", "England Premier League"))

season_data = understat.scrape_all_teams_data("2023/2024", "England Premier League")

with open("season_data.json", "w") as f:
    json.dump(season_data, f, indent=4)