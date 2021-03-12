# We wish to create a program to help Beep and Bop record what they can see in the distance.
# The first function should be named observed and should have no parameters.
from typing import Set


def observed():
    # The function should create a set named observations
    observations = set(["Flying Car", "Sky Scraper", "Sky Scraper", "Laser", "Dome", "Dome"])
    # Finally, the function should return the set observations.
    return observations

# The second function should be named run and should have no parameters.
def run():
    # The function should call the first function and display the set returned by the call.
    print(observed())

if __name__ == "__main__":
    run()
