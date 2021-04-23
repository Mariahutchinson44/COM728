import matplotlib.pyplot as plt
import random as rnd

def data():
    paths = {}
    print("What type of line would you like (:, -- or -)?")
    line_style = input()
    print("What colour would you like (r, g or b)?")
    colour = input()
    print("What marker style would you like (o, s or ^)?")
    marker_style = input()

    paths['line_style'] = line_style
    paths['colour'] = colour
    paths['marker_style'] = marker_style
    return paths

def generate():
    print("How many lines would you like to display?")
    num_lines = int(input())
    for line in range(num_lines):
        values = data()
        # generates 5 random numbers between 1 and 10
        x = rnd.sample(range(1, 10), 5)
        y = rnd.sample(range(1, 10), 5)
        style = f"{values['colour']}{values['line_style']}{values['marker_style']}"
        plt.plot(x, y, style)
    plt.show()

def run():
    print("Running...")
    generate()
    print("Done!")

if __name__ == "__main__":
    run()