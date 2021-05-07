import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()


def animate(frame):
    print(f'Frame: {frame}')


# your code here

def run():
    global fig
    # your code here (use fig with animation function)
    animated = animation.FuncAnimation(fig, animate, frames=10, interval=1000)
    plt.show()


if __name__ == "__main__":
    run()

