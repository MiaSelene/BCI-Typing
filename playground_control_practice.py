import numpy
from matplotlib import pyplot as plt
from matplotlib import animation

from controller import get_data

fig = plt.figure()
ax = plt.axes(xlim=(-1, 1), ylim=(-1, 1))
point, = ax.plot([], [], 'ro', lw=2)
fps = 100
data_generator = get_data()
numpy.random.seed(1)
wx = numpy.random.randn(8) * 2
wy = numpy.random.randn(8) * 2
x, y = 0, 0
# initialization function: plot the background of each frame. Repeats every second
def init():
    point.set_data([], [])
    return point,

# animation function.  This is called sequentially
def animate(i):
    global x
    global y
    data = next(data_generator)
    x += numpy.dot(data, wx)*0.0001
    y += numpy.dot(data, wy)*0.0001
    point.set_data([x], [y])
    return point,

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=fps, interval=int(1000/fps), blit=True)

plt.plot()
plt.show()
