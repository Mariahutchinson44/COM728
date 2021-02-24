def run():
    # We wish to create a program that allows us to display a phrase in reverse
    # displaying the message to ask user for the phrase
    print("What phrase do you see?")
    # read in the user's response
    phrase = input()
    # use a for loop to display the phrase in reverse.
    print("\nReversing...\n")
    # placed before the for loop as only want it to display once and on the same line
    print(f"The phrase is:", end="")
    reversed = ""
    for character in phrase:
        # displays phrase in reverse on same line
        reversed = character + reversed
    print(reversed)
    # I did struggle to understand WHY and HOW this reversed but my son explained