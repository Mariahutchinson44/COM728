def run():
    # ask user how many live cables to avoid.
    print("How many live cables must I avoid?")
    live_cables = int(input())
    # create a variable to track the number of live cables and set this to 0.
    count = 0
    while count < live_cables:
        print("Avoiding...", end="")
        # Increment the variable for tracking the number of live cables
        count = count + 1
        # Display the message with current number of live cables avoided.
        print(f"...Done! {count} live cable avoided!")
    print("All live cables have been avoided.")