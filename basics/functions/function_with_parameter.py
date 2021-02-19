# We wish to create a program that will help Beep and Bop find a way to escape.
# Define a function that has the name escape_by and which takes 1 parameter named plan.
def escape_by(plan):
    # Decide which message to display
    if plan == "jumping over":
        print("We cannot escape that way! The boulder is too big!")
    elif plan == "running around":
        print("We cannot escape that way! The boulder is moving too fast!")
    elif plan == "going deeper":
        print("That might just work! Let's go deeper!")
    else:
        print("We cannot escape that way! The boulder is in the way!")
# calls to your escape function as follows:
escape_by("jumping over")
escape_by("running around")
escape_by("going deeper")