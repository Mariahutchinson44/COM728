def run():
    # Let's boost Beep's health
    old_lives = 3
    old_energy = 10
    old_shield = 7
    print("Beep's current health as of the last activity report is")
    print(f"Lives: {'♥' * old_lives}")
    print(f"Energy: {'♦' * old_energy}")
    print(f"Shield: {'♦' * old_shield}")
    print("Please update the activity report")
    print("Please enter how many charges Beep's batteries have had since the last update?")
    charge = int(input())
    print("Please enter Beep's activity time in hours (out of stand by mode) since last update")
    activity = int(input())
    print("Please enter the amount checks for software updates")
    software = int(input())
    lives = old_lives + charge
    energy = old_energy - activity
    shield = old_shield + software
    print("Updated health has been calculated")
    print(f"Lives: {'♥' * lives}")
    print(f"Energy: {'♦' * energy}")
    print(f"Shield: {'♦' * shield}")
