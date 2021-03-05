# The first function should be named directions and should have no parameters.
def directions():
    directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    # Finally, the function should return the list directions.
    return (directions)


# The second function should be named menu and should have no parameters.
def menu():
    print("Please select a direction:")
    # The function should then call the first function and store the returned list in a local variable
    direction = directions()

    # The function should then use a loop to display each direction in the list with an index number.
    for index in range(len(direction)):
        data = direction[index]
        print(f"{index}: {data}")


def run():
    menu()


if __name__ == "__main__":
    run()
