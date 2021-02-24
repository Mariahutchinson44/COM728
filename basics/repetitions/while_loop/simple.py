def run():
    # Ask user how many cables
    print("How many cables should I remove?")
    cables = int(input())
    # variable created to track number of cables, set to zero
    iteration = 0
    while iteration < cables:
        # increments variable until it matched number of cables
        iteration = iteration + 1
        # displays message each iteration
        print("Removed cable.")
