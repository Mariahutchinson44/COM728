def run():
    # We wish to create a program to help Bop retrieve some numbers and calculate their sum.
    # displaying the message to ask how many number to add up
    print("How many numbers should I sum up?")
    # retrieve the user's response.
    quantity = int(input())
    # variable to count to number of iterations
    count = 0
    # variable to store the answer, i.e. the sum of the numbers
    answer = 0
    # while loop as ask for the required number inputs
    while count < quantity:
        # increase count by one, when count = quantity the correct number of numbers have been input
        count = count + 1
        print(f"Please enter number {count} of {quantity}")
        number = int(input())
        # as each number is input, it is added to the answer
        answer = answer + number
    # display the message
    print(f"The answer is {answer}")