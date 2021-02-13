# We wish to create a program that counts down the distance (in number of steps) to the cave.
# displaying the message
print("How far are we from the cave (in steps)?")
# read in the user's response (a distance in steps)
distance = int(input())
# use a for loop to display the number of steps remaining.
# start is the variable input, stop is zero and count down in -1 step
for count in range (distance, 0, -1):
    # count will decrease by one each time
    print(f"{count} steps remaining")
# display message when zero steps remaining
print("\nWe have reached the cave!")
