# We wish to create a program to determine the ASCII character represented by an ASCII code.
# display the message
print("Program Started!")
print("Please enter an ASCII code:")
# The program should then read in the user's response which should be a positive integer.
code = int(input())
# You can can use the built-in functions abs() and int() to convert the input appropriately.
# The program should then check that the number is in the range 32 - 126 (inclusive) i.e. the printable characters.
# You should use the keyword in and the built-in function range to help you with this.
# If the number in within the range then the program should
if code >=32 and code <= 126:
    # determine the ASCII character from the number using the built-in function chr() to covert.
    # display the message "The character represented by the ASCII code {code} is {character}." where {code} is the number entered by the user and {character} is the ASCII character represented by the number.
    print(f"The character represented by the ASCII value {code} is {chr(code)}")
    # Otherwise, if the number is within the range then the program should
else:
    print("Error! You have not entered a correct code")
print("Program Ended!")