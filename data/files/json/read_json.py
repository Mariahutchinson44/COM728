import json

def read(file_path):
    with open(file_path) as file:
        data = json.load(file)

        # display the name of the city
        city_name = data["city"]
        print(f"City Name: {city_name}")

        # display population
        population = data["population"]
        print(f"Population size: {population}")
        bots = data["bots"]

        #display stats for all bots
        for bot in bots:
            bot_name = bot["name"]
            stats = bot["stats"]
            print(f"{bot_name} has the following stats:{stats}")

#call first function
def run():
    read("robocity.json")

if __name__ == "__main__":
  run()
