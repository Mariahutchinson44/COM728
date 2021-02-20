# program to help Bop climb the bridge ladder, containing 2 functions
def display_ladder(steps):
    #displays each step
    for step in range(steps):
        print("| |")
        print("***")
    # displays bottom of ladder
    else:
        print("| |")
# asks for number of steps remaining, and calls first function
def create_ladder():
    print("How many steps remain?")
    steps = int(input())
    display_ladder(steps)
# calls second function
create_ladder()