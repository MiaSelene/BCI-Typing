
from matplotlib import pyplot as plt
from matplotlib import animation
import pyautogui

fig = plt.figure()
ax = plt.axes(xlim=(0, 10), ylim=(0, 10))
point, = ax.plot([], [], 'ro', lw=2)
fps = 100

# initialization function: plot the background of each frame. Repeats every second
def init():
    point.set_data([], [])
    return point,

# animation function.  This is called sequentially
def animate(i):
    x, y, = pyautogui.position()
    point.set_data([10*x/1440], [10-10*y/900])
    return point,

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=fps, interval=int(1000/fps), blit=True)

plt.plot()
plt.show()
