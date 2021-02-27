import csv

#first function extracts the names from the csv file
def extract(file_path):
    print("Extracting...")
    with open(file_path) as file:
        csv_reader = csv.reader(file)
        # identify and ignore headings
        next(csv_reader)
        #set variable for extracted names
        names = ""
        for values in csv_reader:
            # extract names only [1] and \n stores on new line
            names += f"{values[1]}\n"
        print("Done! The extracted names are as follows:")
        print(f"\n{names}")


def run():
    extract("bots.csv")


if __name__ == "__main__":
    run()
