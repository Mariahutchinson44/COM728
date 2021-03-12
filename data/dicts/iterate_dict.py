# The first function should be named pattern and should have no parameters.
def pattern():
# The function should create a dictionary named sequences.
# The function should populate the dictionary with the following items: "Short Sequence":3, "Medium Sequence":2, "Long Sequence":1
    sequences = {"Short Sequence":3, "Medium Sequence":2, "Long Sequence":1}
    return sequences
    # Finally, the function should return the dictionary

def display_keys(data):
    print("\nKeys:")
    for key in data:
        print(key)

def display_values(data):
    print("\nValues:")
    for value in data.values():
        print(value)

def display_items(data):
    print("\nPairs:")
    for key, value in data.items():
        print(f"{key}: {value}")

# The second function should be named run and should have no parameters.
# The function should call the first function and display the dictionary returned by the call.
def run():
    sequences = pattern()
    print(sequences)
    display_keys(sequences)
    display_values(sequences)
    display_items(sequences)


if __name__ == "__main__":
    run()
