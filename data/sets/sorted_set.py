# The first function should be named observed and should have no parameters.
# The function should create a list named observations.
# The function should populate the list with 5 values read in from the user. There should be some duplicate values.
# Finally, the function should return the list named observations.
def observed():
    observations = []
    for count in range (5):
        print("Please enter an observation:")
        observations.append(input())
    return observations

# The second function should be named remove_observations and should take 1 parameter.
# The parameter should represent the list of observations.
# The function should ask the user if they wish to remove observations.
# While the user wishes to remove observations, the function should
#     Prompt the user to enter a string representing the observation (e.g. "Skyscraper") to be removed
#     The observation should then be removed from the list
def remove_observations(observations):
    keep_asking = True
    while(keep_asking):
        print("Do you wish to remove an observation (yes/no?")
        response = input()
        if response == "yes":
            print("What observation do you wish to remove?")
            observation = input()
            observations.remove(observation)
            print("Done!")
        else:
            keep_asking = False

# The third function should be named run and should have no parameters.
# The function should start by displaying the message "Counting observations...".
# The function should then call the first function and store the returned list in a local variable.
def run():
    print("Counting observations...")
    observations = observed()
    remove_observations(observations)
    # The function should then create a set that contains a tuple for each unique value in the list along with a count for how many times that value appeared in the list e.g. ("Skyscraper", 2)
    observations_set = set()
    for observation in observations:
        data = (observation, observations.count(observation))
        observations_set.add(data)
        #duplicates will be ignored
        # Finally, the function should display the content of the set.
    sorted(observations_set)

    for data in observations_set:
        print(f"{data[0]} observed {data[1]} times.")

if __name__ == "__main__":
    run()
