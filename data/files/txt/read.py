def display_chars(file_path, num_characters):
    with open(file_path) as file:
        partial_data = file.read(num_characters)
        print(f"The first {num_characters} characters are:")
        print(partial_data)

def display_line(file_path):
    with open(file_path) as file:
        line = file.readline().strip()
        print("The first line if:")
        print(line)

def display_text(file_path):
    with open(file_path) as file:
        full_text = file.read
        print("The full text is:")
        print(full_text)

def run():
    display_chars("library.txt", 5)
    display_line("library.txt")
    display_text("library.txt")

if __name__ == "__main__":
    run()