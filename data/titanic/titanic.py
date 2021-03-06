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

def run():
    num_records = load_data("titanic.csv")
    print(f"Successfully loaded {num_records} records.")


if __name__ == "__main__":
    run()
