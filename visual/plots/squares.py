import matplotlib.pyplot as plt

def small():
    x = [3, 4, 4, 3, 3]
    y = [3, 3, 4, 4, 3]
    plt.plot(x, y, 'ro--')

def medium():
    a = [2, 5, 5, 2, 2]
    b = [2, 2, 5, 5, 2]
    plt.plot(a, b, 'gs--')

def large():
    p = [1, 6, 6, 1, 1]
    q = [1, 1, 6, 6, 1]
    plt.plot(p, q, 'bx-')

def run():
    small()
    medium()
    large()
    plt.show()

if __name__ == "__main__":
    run()
