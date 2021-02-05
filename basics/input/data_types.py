# Read input to display user BMI
print("what is your name?")
name = input()
print(f"Hello {name}, what is your age in years?")
user_age = int(input())
print(f"Thank you {name}. Please now enter your height in meters")
user_height = float(input())
print(f"Thank you {name}. One last question - how much do you weigh in kilograms?")
user_weight = float(input())
# calculate BMI
bmi = user_weight / (user_height ** 2)
# display result
print(f"Thank you {name}, you are {user_age} years old and your BMI is {bmi:.2f}")



