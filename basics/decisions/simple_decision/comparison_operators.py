def run():
    # Enter first number
    print("Please enter a first whole number.")
    first_number = int(input())
    # enter second number
    print("Please enter a second whole number.")
    second_number = int(input())
    # display the appropriate message
    if first_number > second_number:
        print("The second number is the smallest")
    elif first_number < second_number:
        print("The first number is the smallest")
    else:
        print("Both are equal!")