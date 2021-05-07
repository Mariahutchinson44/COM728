import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()


def animate(frame):
    global ax
    # your code here (use ax to draw)
    ax.cla()
    x = range(1, 10, 1)
    y = range(1, 10, 1)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)

    ax.plot(x[:frame], y[:frame], 'ro')


def run():
    global fig
    # your code here (use fig with animation function)
    animated = animation.FuncAnimation(fig, animate, frames=10, interval=1000)

    plt.show()


run()
git