# We wish to create a program to help Beep and Bop climb the bridge ladder.
# defining a function that has the name climb_ladder and which takes 2 parameters
    #representing the number of steps remaining and the number of steps crossed.
def climb_ladder(steps_remaining, steps_crossed):
    # display appropriate message
    if steps_remaining > steps_crossed:
        print("Still some way to go!")
    else:
        print("We are almost there!")
# call function
climb_ladder(5, 2)
climb_ladder(2, 5)