import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# class to handle simulated realtime data and plotting
class RealtimePlotting():
	def __init__(self):
		# simulated realtime data function
		self.x = lambda t: 5 * np.sin(2 * np.pi * t)
		self.h = lambda t: 3 * np.pi * np.exp(-self.x(t))

		# define the timestep
		self.t_k = 0.1

		# initialise time and storing arrays
		self.ts = np.array([0])
		self.hs = np.array([self.h(0)])

		self.figure = plt.figure()
		self.line, = plt.plot(self.ts, self.hs)

	def update(self, frame):
		"""
		Called every frame of animation. Updates the figure and data.
		"""

		# set line data
		self.line.set_data(self.ts, self.hs)
		# rescale figure
		self.figure.gca().relim()
		self.figure.gca().autoscale_view()

		# calculate current time
		t = self.ts[-1] + self.t_k
		# update the arrays
		self.ts = np.append(self.ts, t)
		self.hs = np.append(self.hs, self.h(t))

		# animation expects line
		return self.line,

	def plot(self):
		"""
		Calls the animation for realtime plotting.
		"""
		# create the animation using figure and update method
		animation = FuncAnimation(self.figure, self.update, interval=self.t_k * 1000)
		# requires show call
		plt.show()

if __name__ == "__main__":
	plot = RealtimePlotting()
	plot.plot()