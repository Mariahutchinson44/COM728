def run():
    # We wish to create a program to help Beep and Bop cross the bridge.

    # Define a function that has the name cross_bridge and which takes 1 parameter representing the distance of the bridge crossed (in steps).
    def cross_bridge(steps):
        # print message for each step crossed
        for step in range (steps):
            print("Crossed step")
        # displays appropriate message
        if steps > 5:
            print("The bridge is collapsing")
        else:
            print("we must keep going!")
    # call function
    cross_bridge(3)
    cross_bridge(6)
