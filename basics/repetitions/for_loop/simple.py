def run():
    # We wish to create a program that allows us to display some mountains.
    # ask user for the number of mountains
    print("How many mountains should I display?")
    # read in the user's response
    mountains = int(input())
    print("\n Displaying...")
    # use a for loop to display the specified number of ASCII mountains
    for count in range (mountains):
        print("""
               __
              /  \\_
             / ^   \\
            /   ^    \\_
         _ / ^  ^     ^ \\
        /   ^       ^    \\
        """)