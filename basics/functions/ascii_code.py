# We wish to create a program that determines the ASCII code for a character.

# display the message
print("Program Started!")
print("Please enter a standard character:")
# read in the user's response which should be a single character.
letter = input()

# The program should then check that a single letter has been entered using the built-in function len() .

if  len(letter) == 1:
    # determine the ASCII code of the character using the built-in function ord().
    value = ord(letter)
    # display the message "The ASCII code for {letter} is {value}." where {letter} is the letter entered by the user and {value} is the ASCII code as a number.
    print(f"The ASCII code for {letter} is {value}")
    # Otherwise, if the length is not 1 then the program should
    #     display a suitable error message
else:
    print("Error! You must enter a single character.")
# Finally, the program should display the message "Program Ended!".
print("Program ended!")