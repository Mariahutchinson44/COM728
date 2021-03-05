#We wish to create a program to help Beep and Bop cross the falling steps.
# The first function should be named steps and should have no parameters.
def steps():
    likelihoods = [
    ("step 1", 50),
    ("step 2", 38),
    ("step 3", 27),
    ("step 4", 99),
    ("step 5", 4)
    ]
    # Finally, the function should return the list of tuples.
    return likelihoods

# The second function should be named run and should have no parameters.
def run():
    # The function should call the first function and store the returned list in a local variable.
    data = steps()
    # The function should then create two empty lists, good_steps and bad_steps.
    good_steps = []
    bad_steps = []
    # if the likelihood of the step falling is 50 or more then add the tuple to bad_steps
    for step in data:
        if step[1] >= 50:
            bad_steps.append(step)
        #otherwise add the tuple to good_steps
        else:
            good_steps.append(step)
    # Finally, the function should display a message
    print(f"Good steps: {len(good_steps)}, Bad steps: {len(bad_steps)}")

if __name__ == "__main__":
    run()