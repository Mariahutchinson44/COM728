# The first function should be named observed and should have no parameters.
# The function should create a list named observations.
# The function should populate the list with 7 values read in from the user. There should be some duplicate values.
# Finally, the function should return the list named observations.
def observed():
    observations = []
    for count in range (7):
        print("Please enter an observation:")
        observations.append(input())
    return observations

# The second function should be named run and should have no parameters.
# The function should start by displaying the message "Counting observations...".
# The function should then call the first function and store the returned list in a local variable.
def run():
    print("Counting observations...")
    observations = observed()
    # The function should then create a set that contains a tuple for each unique value in the list along with a count for how many times that value appeared in the list e.g. ("Skyscraper", 2)
    observations_set = set()
    for observation in observations:
        data = (observation, observations.count(observation))
        observations_set.add(data)
        #duplicates will be ignored
        # Finally, the function should display the content of the set.
    for data in observations_set:
        print(f"{data[0]} observed {data[1]} times.")

if __name__ == "__main__":
    run()
