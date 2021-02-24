import basics.output.simple_message as simple_message
import basics.output.multiline_message as multiline_message
import basics.output.escape_characters as escape_characters
import basics.output.ascii_art as ascii_art
import basics.input.ascii_robot as ascii_robot
import basics.input.data_types as data_types
import basics.input.review as review_input
import basics.input.string_operators as string_operators
import basics.input.user_input as user_input
import basics.decisions.review as review_decisions
import basics.decisions.or_operator as or_operator
import basics.decisions.and_operator as and_operator

def run_block_a():
    print("Which program in 'Block A: Basics' do you wish to run?")
    response = input()
    if response == "simple_message":
        simple_message.run()
    elif response == "multiline_message":
        multiline_message.run()
    elif response == "escape_characters":
        escape_characters.run()
    elif response == "ascii_art":
        ascii_art.run()
    elif response == "ascii_robot":
        ascii_robot.run()
    elif response == "data_types":
        data_types.run()
    elif response == "review_input":
        review_input.run()
    elif response == "string_operators":
        string_operators.run()
    elif response == "user_input":
        user_input.run()
    elif response == "review_decisions":
        review_decisions.run()
    elif response == "or_operator":
        or_operator.run()
    elif response == "and_operator":
        and_operator.run()





def run():

    while(True):
        print("What would you like to do?")
        print("[a] Run 'Block A: Basics' programs")
        print("[q] Quit")
        response = input()

        if response == "a":
            run_block_a()
        elif response == "q":
            break
        else:
            print("Invalid option! Please try again.")

run()