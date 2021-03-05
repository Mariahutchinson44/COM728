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
        # The function should then read in the user's response.
    #remember response should be an integer
    response = int(input())
    return direction[response]


# The third function should be named run and should have no parameters.
def run():
    # The function should create an empty list named route.
    route = []
    print("Working out escape route...")
    # The function should then use a loop to do the following 5 times:
    iteration = 0
    while iteration < 5:
        # increments variable until it matches number
        iteration = iteration + 1
        # displays message each iteration
        # Call the function menu and append the returned direction to the list route.
        route.append(menu())
    # Finally, the function should display the message
    print(f"Escape route: {route}")


if __name__ == "__main__":
    run()
