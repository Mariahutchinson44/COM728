# ask the user to enter a sequence of characters
print("Please enter a sequence (consisting of dashes and two markers)")
sequence = input()
# ask the user to enter a character representing the marker
print("Please enter the character for the marker")
marker = input()
# find the markers
start_counting = False
count = 0
# The program should then count the number of dashes between the two markers.
for character in sequence:
    #do not start counting until for marker found
    if (start_counting == False) and (character == marker):
        # first marker found, so start counting
        start_counting = True
    # second marker found so display count
    elif (start_counting == True) and (character == marker):
        print(f"The distance between the markers is {count}")
    # second marker not found so increment count
    elif start_counting:
        count = count + 1








