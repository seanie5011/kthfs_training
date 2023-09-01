import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# simulated realtime data function
x = lambda t: 5 * np.sin(2 * np.pi * t)
h = lambda t: 3 * np.pi * np.exp(-x(t))

# define the timestep
t_k = 0.001

# initialise time and storing arrays
t = 0
ts = [t]
hs = [h(t)]

figure = plt.figure()
line, = plt.plot(ts, hs)

def update(frame, *fargs):
	line.set_data(ts, hs)
	figure.gca().relim()
	figure.gca().autoscale_view()

	# update the arrays and timestep
	# calculate current time
	# fargs[0] is the timestep
	t = ts[-1] + fargs[0]
	ts.append(t)
	hs.append(h(t))

	return line,

animation = FuncAnimation(figure, update, interval=t_k * 1000, fargs=[t_k])

plt.show()