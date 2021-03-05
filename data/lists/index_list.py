# The first function should be named movements and should have no parameters.
def movements():
    path = ["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
    return (path)


# The second function should be named run and should have no parameters.

def run():
    print("Moving...")
    data = movements()
    # The function should then call the first function and store the return list in a local variable
    # The function should then display the values in the list in the following format:
    print(f"{data[0]} for {data[1]} steps")
    print(f"{data[2]} for {data[3]} steps")
    print(f"{data[4]} for {data[5]} steps")
    print(f"{data[6]} for {data[7]} steps")
    # where {direction} is the direction of movement and {steps} is the number of steps to move.


if __name__ == "__main__":
    run()
