import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig, ax = plt.subplots()


def animate(frame):
    global ax
    ax.set_xlim(0, 720)
    ax.set_ylim(-1, 1)
    x_in_degrees = np.arange(0, frame)
    x_in_radians = x_in_degrees * (np.pi / 180)
    y = np.sin(x_in_radians)
    ax.plot(x_in_degrees, y)


def run():
    global fig
    sine_animation = animation.FuncAnimation(fig, animate, frames=720, interval=100)
    plt.show()


run()

# you can tell it is animating as the colours keep changing as it selects random ones
