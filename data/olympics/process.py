import tui

def list_years(data):
    tui.started("Listing years")
    # create set (will ignore duplicates)
    years = set()
    for record in data:
        year = record[9]
        years.add(year)
    tui.display_years(years)
    tui.completed()

def tally_medals(data):
    tui.started("Tallying medals")
    # create dictionary
    tally = {"Gold": 0, "Silver": 0, "Bronze": 0}
    for record in data:
        medal = record[14]
        if medal in ("Gold", "Silver", "Bronze"):
            tally[medal] += 1
    tui.display_medal_tally(tally)
    tui.completed()

def tally_team_medals(data):
    tui.started("Tallying medals for each team.")
    # create nested dictionary
    team_tally = {}
    for record in data:
        team = record[6]
        medal = record[14]
        if medal not in ("Gold", "Silver", "Bronze"):
            continue
        # if team already in dictionary, increment count
        if team in team_tally:
            team_tally[team][medal] += 1
        #if not already on dictionary, add team then increment count
        else:
            team_tally[team] = {"Gold": 0, "Silver": 0, "Bronze": 0}
            team_tally[team][medal] += 1
    tui.display_team_medal_tally(team_tally)
    tui.completed()