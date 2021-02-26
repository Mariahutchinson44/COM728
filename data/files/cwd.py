# We wish to create a program to display information about the current working directory.
# The first function should be named cwd and should have no parameters.

def cwd():
    # The function should retrieve the file path for the current working folder.
    import os
    path = os.getcwd()

    # display the message
    print(f"Current Working directory is {path}")

    # display the message
    print("The directory contains the following files:")

    # Finally, the function should display each file contained in the current working directory.
    for file in os.listdir(path):
        print(file)

#The second function should be named run and should have no parameters.
def run():
    # display the message
    print("Processing...")
    # call the first function.
    cwd()

run()