# We wish to write a program that will allow us to load the data set for processing.
# set global variables
records = []
headings = []


def load_data(file_path):
    # display message, next message on same line
    print("Loading data...", end="")
    # open the file given by file_path for reading
    import csv
    # open file for reading
    with open(file_path) as file:
        csv_reader = csv.reader(file)
        # read and assign headings to global variable
        headings.append(next(csv_reader))
        # set counter for number of records
        num_records = 0
        for value in csv_reader:
            # append each list to global variable
            records.append(value)
            num_records = num_records + 1
    print("Done!")
    return num_records

def display_menu():
    print("""
    Please select one of the following options:
    [1] Display the names of all passengers
    [2] Display the number of passengers that survived
    [3] Display the number of passengers per gender
    [4] Display the number of passengers per age group

    """)
    response = int(input())
    return response

def run():
    num_records = load_data("titanic.csv")
    print(f"Successfully loaded {num_records} records.")
    selected_option = display_menu()
    print(f"You have selected option: {selected_option}")

if __name__ == "__main__":
    run()
