# first function takes 2 parameters, file path and number of characters to be read.
def display_chars(file_path, num_characters):
    # open file for reading (and will automatically close)
    with open(file_path) as file:
        # read in user specified number of characters
        partial_data = file.read(num_characters)
        # display message
        print(f"The first {num_characters} characters are:")
        print(partial_data)

# second function takes one parameter, file path
def display_line(file_path):
    # open file for reading (and will automatically close)
    with open(file_path) as file:
        line = file.readline().strip()
        # display message
        print("The first line if:")
        print(line)

def display_text(file_path):
    # open file for reading (and will automatically close)
    with open(file_path) as file:
        full_text = file.read()
        # display message
        print("The full text is:")
        print(full_text)

def run():
    display_chars("library.txt", 5)
    display_line("library.txt")
    display_text("library.txt")

if __name__ == "__main__":
    run()