import numpy as np
import matplotlib.pyplot as plt
import time

# simulated realtime data function
x = lambda t: 5 * np.sin(2 * np.pi * t)
h = lambda t: 3 * np.pi * np.exp(-x(t))

# define the timestep
t_k = 0.1

# initialise time and storing arrays
t = 0
ts = np.array([t])
hs = np.array([h(t)])

# loop to increase time
while t < 100:
	# plot the graph
	plt.plot(ts, hs)

	# pause to both sleep for simulation
	# and to keep graph up
	# place before updating values to keep consistency
	plt.pause(t_k)

	# update the arrays and timestep
	t += t_k
	ts = np.append(ts, t)
	hs = np.append(hs, h(t))

plt.show()