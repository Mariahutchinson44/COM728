def run():
    # first function to sum the weights
    def sum_weights(beep_weight, bop_weight):
        total_weight = beep_weight + bop_weight
        # returns value of the total weight
        return total_weight
    # second function averages the weight
    def calc_avg_weight(beep_weight, bop_weight):
        # calls first function and uses value
        average_weight = (sum_weights(beep_weight, bop_weight))/2
        # returns value of average weight
        return average_weight
    # third funtion asks for user to input weights
    def run():
        print("What is the weight of Beep?")
        beep_weight = float(input())
        print("What is the weight of Bop?")
        bop_weight = float(input())
        # asks user which action should be used
        print("What would you like to calculate (sum or average)?")
        calculation = input()
        # decides on action
        if calculation == "sum":
            answer = sum_weights(beep_weight, bop_weight)
            # answer:.2f gives to 2 decimal places
            print(f"The sum of Beep and Bop's weight is {answer:.2f}")
        elif calculation == "average":
            answer = calc_avg_weight(beep_weight, bop_weight)
            # answer:.2f gives to 2 decimal places
            print(f"The average of Beep and Bop's weight is {answer:.2f}")
        else:
            print("Please enter sum or average")

    # Run program
    run()
