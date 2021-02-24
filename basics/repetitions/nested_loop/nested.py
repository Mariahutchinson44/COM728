def run():
    # We wish to create a program that allows us to display a grid of ASCII emoji.
    # ask the user how many rows and columns
    print("How many rows should I have?")
    rows = int(input())
    print("How many columns should I have?")
    columns = int(input())
    print("\nHere I go:\n")
    # The program should then display a grid of ascii emoji
    # where the size of grid matches the number of rows and columns specified by the user
    # for loop will repeat for the number of required rows
    for row_number in range(0, rows, 1):
        # for loop will repeat for required columns....
        for column_number in range(0, columns, 1):
            #...printing them on same line
            print(f":-)", end="")
        print()
    print("\nDone!")