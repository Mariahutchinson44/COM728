def run():
    # ask user how many bars should be charged
    print("How many bars should be charged?")
    # read in the user's response.
    bars = int(input())
    # create a variable to track the number of bars charged and set this to 0.
    count = 0
    # use a while loop
    while count < bars:
        # Display message, next message will print on same line
        print("Charging:", end="")
        # Increment the variable for tracking the number of charged bars.
        count = count + 1
        # Display the number of charged bars, space added between bars
        print(f"{' █ ' * count}")
    # display the message on a new line
    print("\n The battery is fully charged.")