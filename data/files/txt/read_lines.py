# first function take 1 parameter that represents a file name.
def search(file_name):
    #display message
    print("Searching...")

    # The function should then open the specified file for reading.
    with open(file_name) as file:
        #For each line in the file:
        for line in file:
            location = line.strip()
            # display the message where {location} is a line from the file.
            print(f"Looked in {location}")
        # display the message
        print("...Done!")

def run():
# The function should call the first function with the path to the file library.txt.
    search("library.txt")

run()