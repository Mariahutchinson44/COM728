
# displays word in a box
def display_in_box(word):
    message = f"* {word} *"
    print("*" * (len(message)))
    print(message)
    print("*" * (len(message)))

# displays word lower case by adding .lower()
def display_lower_case(word):
    # lower case
    print(word.lower())

# displays word upper case by adding .upper()
def display_upper_case(word):
    print(word.upper())

# display word mirrored
def display_mirrored(word):
    mirrored = ""
    # to reverse the letters in the word
    for letter in reversed(word):
        mirrored = mirrored + letter
    print(f"{word} | {mirrored}")

# ask user how many times to repeat
def repeat(word):
    print("How many times should the word be repeated")
    times = int(input())
    for repeat in range(times):
        #if number % 2 == 0 it is an even number
        if repeat % 2 == 0:
            # calls function which will print lower case word
            display_lower_case(word)
        # odd repeat
        else:
            # calls function which will print upper case word
            display_upper_case(word)

def run():
    print("Please enter a word")
    word = input()
    # get users selection
    print("""
    Please choose one of the following 5 options:
    1) Display in a Box
    2) Display Lower-case
    3) Display Upper-case 
    4) Display Mirrored
    5) Repeat 
    """)
    option = int(input())
    if option == 1:
        display_in_box(word)
    elif option == 2:
        display_lower_case(word)
    elif option == 3:
        display_upper_case(word)
    elif option == 4:
        display_mirrored(word)
    elif option == 5:
        repeat(word)
    else:
        print("Invalid option")
# run()