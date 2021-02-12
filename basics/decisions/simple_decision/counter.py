# Enter first number
print("Please enter a first whole number.")
first_number = int(input())
# enter second number
print("Please enter a second whole number.")
second_number = int(input())
# enter third number
print("Please enter a third whole number.")
third_number = int(input())
even_numbers = 0
odd_numbers = 0
# check which numbers are even or odd
if first_number % 2 == 0:
    even_numbers = even_numbers + 1
else:
    odd_numbers = odd_numbers + 1

if second_number % 2 == 0:
    even_numbers = even_numbers + 1
else:
    odd_numbers = odd_numbers + 1

if third_number % 2 == 0:
    even_numbers = even_numbers + 1
else:
    odd_numbers = odd_numbers + 1

# Display correct result
print(f"There were {even_numbers} even and {odd_numbers} odd numbers.")
