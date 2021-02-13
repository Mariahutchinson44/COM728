# We wish to create a program that adjusts the light level of Beep and Bop's night vision.
# display the message to ask user brightness level
print("What level of brightness is required (even number)?")
# read in the user's response (an even number representing the brightness level)
brightness = int(input())
# range of even numbers between 2 and the number entered by the user.
print("Adjusting brightness...\n")
# range will not include stopping value, hence adding 1 to include it
for count in range (2, (brightness + 1), 2):
    # count will start at 2 * and repeat in 2s until required brightness met
    print(f"Beep's brightness level: {'*' * count}")
    print(f"Bop's brightness level: {'*' * count}\n")
print("Adjustments complete!")