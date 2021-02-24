def run():
    # We wish to create a program to help Beep and Bop escape the large boulder.
    # The program should start by defining a function that has the name identify and which takes 0 parameters.
    def identify():
    # The function should do the following:
        # Ask the user to enter a word representing what they see.
        print("What lies before us?")
        # Read the user's response.
        response = input()
        # If the user's response is "a large boulder" then the message "It's time to run!" should be displayed.
        if response == "a large boulder":
            print("It's time to run!")
            # Otherwise the message "We will be fine." should be displayed.
        else:
            print("We will be fine")
    # Finally, the program should contain a call to your identify function.
    identify()
