import matplotlib.pyplot as plt

def display(x_values, y_values):
    plt.plot(x_values, y_values)
    plt.show()

def run():
    x = [1, 2, 3, 4, 5]
    y = [1, 4, 9, 16, 25]
    display(x, y)

if __name__ == "__main__":
    run()
