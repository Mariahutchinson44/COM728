def started(msg=""):
    print("-" * 85)
    print(f"Operation started: {msg}...\n")


def completed():
    print("\nOperation completed.")
    print("-" * 85)


def error(msg):
    print(f"Error! {msg}")


def menu():
    print("""
    Please select one of the following options:
        [years]     List unique years
        [tally]     Tally up medals
        [team]      Tally up medals for each team
        [exit]      Exit the program
        
    Your selection:
    """)
    selection = input()
    return selection.strip().lower()


def display_medal_tally(tally):
    # tally is a dictionary, keys = medal names and value = medal counts
    print(f"|{'Gold':<10} | {tally['Gold']:<10}|")
    print(f"|{'Silver':<10} | {tally['Silver']:<10}|")
    print(f"|{'Bronze':<10} | {tally['Bronze']:<10}|")


def display_team_medal_tally(team_tally):
    # team tally is a nested dictionary
    # unpack the dictionary in to team and tally
    for team, tally in team_tally.items():
        print(team)
        print(f"\tGold:{tally['Gold']}, Silver:{tally['Silver']}, Bronze:{tally['Bronze']}")

def display_years(years):
    # years is a set containing integer values, sort in descending order, on a new line
    sorted_years = sorted(years, reverse=True)
    for year in sorted_years:
        print(year)

started("test")
completed()
error("Invalid Selection!")
menu()
display_medal_tally({'Gold': 1, 'Silver': 3, 'Bronze': 4})

display_team_medal_tally({'United Kingdom': {'Gold': 10, 'Silver': 5, 'Bronze': 2}})
display_years((2000, 2000, 2001, 2003))
