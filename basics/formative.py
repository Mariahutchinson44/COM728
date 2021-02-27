def setup():
    #display message
    print("Setting up the Pokedex...")
    print("Enter the trainer's name:")
    # User response
    trainer_name = input()
    print(f"{trainer_name}'s Pokedex has been set up.")

setup()

def check(pokemon):
    if pokemon == "Pikachu":
        print("Pokedex: you have a very rare Pokemon.")
    else:
        print("You have found a known Pokemon.")

check("Pikachu")
check("Bulbasaur")

def catch(num_pokemon):
    for count in range(num_pokemon):
        print("Caught Pokemon!")
    print("All Pokemon have been caught!")

catch(3)