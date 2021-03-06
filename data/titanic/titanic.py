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
# Display options and return user response (an integer)
def display_menu():
    print("""
    Please select one of the following options:
    [1] Display the names of all passengers
    [2] Display the number of passengers that survived
    [3] Display the number of passengers per gender
    [4] Display the number of passengers per age group
    [5] Display the number of survivors per age group

    """)
    response = int(input())
    return response

# print passenger names is user response selected option 1
def display_passenger_names():
    print("The names of the passengers are...\n")
    for record in records:
        passenger_name = record[3]
        print(passenger_name)

# increment variable for each survivor and display total
def display_num_survivors():
    num_survived = 0
    for record in records:
        survival_status = record[1]
        if survival_status == "1":
            num_survived += 1
    print(f"{num_survived} passengers survived.")

# increment variables for male/female and display results
def display_passengers_per_gender():
    females = 0
    males = 0
    for record in records:
        gender = record[4]
        if gender == "male":
            males += 1
        else:
            females += 1
    print(f"females: {females}, males: {males}")

def display_passengers_per_age_group():
    children = 0
    adults = 0
    elderly = 0
    for record in records:
        #check if we have an age i.e. check that age is not an empty string
        if len(record[5]) > 0:
            # store age as a float (did not work as integer)
            age = float(record[5])
            if age < 18:
                children += 1
            elif age < 65:
                adults += 1
            else:
                elderly += 1
    print(f"children: {children}, adults: {adults}, elderly: {elderly}")

def display_survivors_per_age_group():
    children = 0
    child_survivors = 0
    adults = 0
    adult_survivors = 0
    elderly = 0
    elderly_survivors = 0

    for record in records:
        # check if we have an age i.e. check that age is not an empty string
        if len(record[5]) > 0:
            # store age as a float (did not work as integer)
            age = float(record[5])
            if age < 18:
                children += 1
                if record[1] == "1":
                    child_survivors += 1
            elif age < 65:
                adults += 1
                if record[1] == "1":
                    adult_survivors += 1
            else:
                elderly += 1
                if record[1] == "1":
                    elderly_survivors += 1
    print(f"children: {child_survivors}/{children}, adults: {adult_survivors}/{adults}, elderly: {elderly_survivors}/{elderly}")

def run():
    num_records = load_data("titanic.csv")
    print(f"Successfully loaded {num_records} records.")
    selected_option = display_menu()
    if selected_option == 1:
        print(f"You have selected option: {selected_option}\n")
        display_passenger_names()
    elif selected_option == 2:
        print(f"You have selected option: {selected_option}\n")
        display_num_survivors()
    elif selected_option == 3:
        print(f"You have selected option: {selected_option}\n")
        display_passengers_per_gender()
    elif selected_option == 4:
        print(f"You have selected option: {selected_option}\n")
        display_passengers_per_age_group()
    elif selected_option == 5:
        print(f"You have selected option: {selected_option}\n")
        display_survivors_per_age_group()
    else:
        print("Error! Option not recognised!")

if __name__ == "__main__":
    run()
