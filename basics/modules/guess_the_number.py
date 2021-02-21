# turned program into a user defined function
def play_guess_the_number():
    #import the module
    import random
    # ask for user input
    print("Please enter the minimum value:")
    min_value = int(input())
    print("Please enter the maximum value:")
    max_value = int(input())
    # generate random number (randrange is a function within the random module)
    random_number = random.randrange(min_value, max_value)
    print(f"I am thinking of a number between {min_value} and {max_value}.")
    print("Can you guess what it is?")
    print("Please enter a number:")
    # set variable to track when correct number is selected
    correct_guess = False
    # while not correct, repeatedly ask for a number
    while not correct_guess:
        guess = int(input())
        # compare guess to random number generated
        if guess == random_number:
            print("Congratulations! You guessed my number!")
            # set variable to true
            correct_guess = True
        elif guess < random_number:
            print("Your guess is too low.")
            print("Try again:")
        else:
            print("Your guess is too high.")
            print("Try again:")

    print("Game over!")

play_guess_the_number()
