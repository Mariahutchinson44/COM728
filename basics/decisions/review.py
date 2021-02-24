def run():
    # Beep is learning about primary and secondary colours
    # Choose 2 primary colours
    print("Please chose your first primary colour (red/blue/yellow)")
    first_colour = input()
    print("Please chose your second primary colour (red/blue/yellow)")
    second_colour = input()
    if not ((first_colour == "red") or (first_colour == "blue") or (first_colour == "yellow")):
        print("Your first colour is not a primary colour")
        if not ((second_colour == "red") or (second_colour == "blue") or (second_colour == "yellow")):
            print("Your second colour is not a primary colour")
    # decide which secondary colour from red (purple or orange)
    if (first_colour == "red") or (second_colour == "red"):
        if ((first_colour == "red") and (second_colour == "blue")) or ((second_colour == "red") and (first_colour == "blue")):
            print(f"The primary colours {first_colour} and {second_colour} make the secondary colour purple")
        elif ((first_colour == "red") and (second_colour == "yellow")) or ((second_colour == "red") and (first_colour == "yellow")):
            print(f"The primary colours {first_colour} and {second_colour} make the secondary colour orange")
        elif (first_colour == "red") and (second_colour == "red"):
            print("You have chosen the same two colours")
    # decide the remaining secondary colour (green)
    elif (first_colour == "blue") or (second_colour == "blue"):
        if ((first_colour == "blue") and (second_colour == "yellow")) or ((second_colour == "blue") and (first_colour == "yellow")):
            print(f"The primary colours {first_colour} and {second_colour} make the secondary colour green")
        elif first_colour == second_colour:
            print("You have chosen the same two colours")
    # only option left would be to choose two yellows
    elif (first_colour == "yellow") or (second_colour == "yellow"):
        print("You have chosen the same two colours")



