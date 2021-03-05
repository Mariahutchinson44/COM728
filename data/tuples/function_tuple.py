# The first function should be named likelihood and should have no parameters.
def likelihood():
    # The function should create a tuple named likelihoods.
    likelihoods = (50, 38, 27, 99, 4)
    # Finally, the function should return the step with the smallest likelihood of falling
    min_value = min(likelihoods)
    max_value = max(likelihoods)
    return min_value, max_value

# The second function should be named run and should have no parameters.
def run():
    # The function should call the first function and stored the returned value in a local variable
    probabilities = likelihood()
    # The function should then display a message in the format:
    print(f"Minimum likelihood of falling: {probabilities[0]}%")
    print(f"Maximum likelihood of falling: {probabilities[1]}%")


if __name__ == "__main__":
    run()