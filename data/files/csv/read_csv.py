import csv
# The first function should take 1 parameter
def read(file_path):
    # open for reading.
    with open(file_path) as file:
        csv_reader = csv.reader(file)
        headings = next(csv_reader)
        # print headings
        print(f"Headings:\n{headings}")
        print("Values:")
        for values in csv_reader:
            print(values)


# second function should be named run and should take no parameters.
def run():
    read("bots.csv")


# add code so it executes the function run when the file is executed directly.
if __name__ == "__main__":
    run()
