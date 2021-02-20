# We wish to create a program that listens for sounds in the cave.
# The program should start by defining a function that has the name listen and which takes 0 parameters.
def listen():
# The function should do the following:
    # Ask the user to enter a word representing a sound
    print("What sound did you hear?")
    sound = input()
    # Display the message followed by the word entered by user and an exclamation mark.
    print(f"That was a loud {sound}!")
# Finally, the program should contain a call to your function listen
listen()