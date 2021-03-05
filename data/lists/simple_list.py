# We wish to create a program to help Beep and Bop find their way through the maze.
# The first function should be named directions and should have no parameters.
def directions():
    # create a list named directions with the following items:
    # "Move Forward", "Move Backward", "Turn Left" and "Turn Right".
    directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    # Finally, the function should return the list directions.
    return (directions)


# The second function should be named run and should have no parameters.
# The function should call the first function and display the list returned by the call.
def run():
    print(directions())


run()
