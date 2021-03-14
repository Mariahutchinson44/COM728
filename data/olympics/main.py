import csv
import process
import tui


def read_data(file_path):
    #code to read specified file path
    tui.started(f"Reading data from {file_path}")
    data = []
    with open(file_path) as file:
        csv_reader = csv.reader(file)
        #ignore first line, i.e. headings
        next(csv_reader)
        for line in csv_reader:
            data.append(line)
    tui.completed()
    return data

def run():
    athlete_data = read_data("athlete_events.csv")

    while True:
        selection = tui.menu()
        if selection == "years":
            pass
        elif selection == "tally":
            pass
        elif selection == "team":
            pass
        elif selection == "exit":
            break
        else:
            tui.error("Invalid Selection!")


if __name__ == "__main__":
    run()