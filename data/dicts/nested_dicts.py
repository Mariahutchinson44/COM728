# The first function should be named short_pattern and should have no parameters.
# Finally, the function should return the dictionary.
def short_pattern():
    pattern = {"sequence":"101", "occurrences":5}
    return pattern

# The second function should be named medium_pattern and should have no parameters.
# The function should create a dictionary named pattern.
# The function should populate the dictionary with the following key-value pairs:
# "sequence":"111000"
# "occurrences": 25
def medium_pattern():
    pattern = {"sequence":"111000", "occurrences": 25}
    return pattern
#should return the dictionary
#
# The third function should be named long_pattern and should have no parameters.
# The function should create a dictionary named pattern.
# The function should populate the dictionary with the following key-value pairs:
# "sequence":"1100110011001100"
# "occurrences":50
def long_pattern():
    pattern = {"sequence":"1100110011001100", "occurrences":50}
    return pattern

# The fourth function should be named run and should have no parameters.
def run():
# The function should start by displaying the message "Analysing patterns...".
    print("Analysing patterns...")
    # The function should then create a dictionary with the following key-value pairs:
    patterns = {"short sequences": short_pattern(), "medium sequences": medium_pattern(), "long sequences": long_pattern()}
# "short sequence": value returned from first function
# "medium sequence": value returned from second function
# "long sequence": value returned from third function
    for key, value in patterns.items():
        print(f"{key}: {value}")
# Finally, the function should display the content of the dictionary as key-value pairs using an appropriate loop
if __name__ == "__main__":
    run()