# We wish to create a program to help Bop calculate the factorial of a specified number.
# ask user for a number
print("Please enter a number:")
number = int(input())
# create 2 variables, one to count to the variable number, and the other to store the answer
count = 0
# started variable at 1, as multiplying by zero for first iteration would give incorrect answer
answer = 1
# use a while loop to calculate the factorial of the specified number.
while count < number:
        count = count + 1
        answer = answer * count
# display the message
print(f"The factorial is {answer}")
