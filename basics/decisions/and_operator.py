def run()
    # Ask what Beep heard
    print("What did I hear?")
    noise = input()
    print("What did I see?")
    sight = input()

    # Identify and display the category
    if (noise == "grrr") and (sight == "two red eyes"):
        print("There is a scary creature. I should get out of here!")
    else:
        print("I am a little scared but I will continue.")