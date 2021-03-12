# The first function should be named pattern and should have no parameters.
def pattern():
# The function should create a dictionary named sequences.
# The function should populate the dictionary with the following items: "Short Sequence":3, "Medium Sequence":2, "Long Sequence":1
    sequences = {"Short Sequence":3, "Medium Sequence":2, "Long Sequence":1}
    return sequences
    # Finally, the function should return the dictionary

# The second function should be named run and should have no parameters.
# The function should call the first function and display the dictionary returned by the call.
def run():
    sequences = pattern()
    print(sequences)


if __name__ == "__main__":
    run()
