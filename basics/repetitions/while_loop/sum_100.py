def run():
    # We wish to create a program to help Bop calculate the sum of the first 100 numbers.
    # display message
    print("Calculating the sum of the first 100 numbers...")
    # create 2 variables, one to count 1 to 100, and the other to store the answer
    count = 0
    answer = 0
    # use while loop to calculate the sum of the first 100 numbers from 1 to 100 (inclusive)
    while count < 100:
        count = count + 1
        answer = answer + count
    # display the message
    print(f"...Done! The answer is {answer}")