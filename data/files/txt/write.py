# first function take 1 parameter that represents a file path.
def search(file_path):
    # display the message
    print("Searching...")
    # create a string variable named sections and set its value to "" (i.e. an empty string)
    sections = ""
    # create a string variable named books and set its value to "Books:\n".
    books = "Book:\n"
    # open the specified file for reading.
    with open(file_path) as file:
    # For each line in the file,
        for line in file:
            # If the line starts with "Section" then
            if line.startswith("Section"):
                sections = sections + line
                # Add the line, including a new line character (\n), to the string sections.
            else:
                # Add the line, including a new line character (\n), to the string books.
                books = books + line
    #display message
    print("Done!")
    # Finally, the function should return a single string consisting of sections and books and two new line characters between them i.e. the returned string should be in the format "{sections}\n\n{books}".
    return f"{sections}\n\n{books}"
# The second function should be named save and should take 2 parameters.
#The first parameter is a file path.
#The second parameter is a string that represents the data to be stored.
def save(file_path, data):
    #display the message
    print("Saving...")
    #The function should then open the specified file for writing.
    with open(file_path, "w") as file:
        # The function should then write the data to the file.
        file.write(data)
        # display the message
        print("Done!")

# The third function should be named run and should have no parameters.
def run():
    # The function should call the first function with the file path "data/files/txt/books.txt" and store the value returned by the function in a local variable named data.
    data = search("books.txt")
    # The function should then pass the variable as an argument to the second function along with the filename "data/files/txt/section-books.txt".
    save("/Users/mariahutchinson/PycharmProjects/COM728/data/files/txt/section-books.txt", data)

run()
