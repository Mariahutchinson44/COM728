def run():
    # We wish to create a program that allows us to display a word character by character.
    # display message to ask user for markings
    print("What strange markings do you see?")
    # read in the user's response
    markings = input()
    print("\nIdentifying...\n")
    for position in range(0, len(markings), 1):
        print(f"index {position}:", markings[position])
    print("\nDone!")
    # Finally, the program should use a for loop to display each character in the user's reponse along with its index position on a new line.