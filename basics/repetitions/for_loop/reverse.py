# We wish to create a program that allows us to display a phrase in reverse.
# displaying the message to ask user for the phrase
print("What phrase do you see?")
# read in the user's response
phrase = input()
# use a for loop to display the phrase in reverse.
print("\nReversing...\n")
# placed before the for loop as only want it to display once and on the same line
print(f"The phrase is:", end="")
# highest position is len(phrase) -1.
# Stop position is -1 otherwise will not display index position zero
# Stepping down in -1 increments
for position in range(len(phrase) -1, -1, -1):
    # displays phrase in reverse on same line
    print(phrase[position], end="")
