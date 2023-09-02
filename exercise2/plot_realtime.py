import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import customtkinter as ctk

# class to handle simulated realtime data and plotting
class RealtimePlotting():
	def __init__(self, frame, row, column, figsize, title):
		# ctk frame to be used
		self.frame = frame
		self.row = row
		self.column = column

		# simulated realtime data function
		self.x = lambda t: 5 * np.sin(2 * np.pi * t)
		self.h = lambda t: 3 * np.pi * np.exp(-self.x(t))

		# define the timestep
		self.t_k = 0.1

		# initialise time and storing arrays
		self.ts = np.array([0])
		self.hs = np.array([self.h(0)])

		# whether we want to collect data initially
		self.collecting_data = True

		# whether to show the grid
		self.use_grid = True

		# the title of the plot
		self.title = title

		# initial plotting parameters and variables
		self.fig, self.ax = plt.subplots(1, 1, figsize=figsize)
		self.line, = self.ax.plot(self.ts, self.hs)

		# start the plotting animation
		self.plot()

	def get_data(self):
		"""
		Returns the current data
		"""

		return self.ts, self.hs

	def update(self, i):
		"""
		Called every frame of animation. Updates the figure and data if needed.
		"""

		# if we are collecting more data to plot
		if self.collecting_data:
			# set line data
			self.line.set_data(self.ts, self.hs)
			# rescale figure
			self.fig.gca().relim()
			self.fig.gca().autoscale_view()

			# calculate current time
			t = self.ts[-1] + self.t_k
			# update the arrays
			self.ts = np.append(self.ts, t)
			self.hs = np.append(self.hs, self.h(t))

		if self.use_grid:
			self.ax.grid(True)
		else:
			self.ax.grid(False)

	def plot(self):
		"""
		Calls the animation for realtime plotting.
		"""

		# set up the canvas to be given for ctk
		self.canvas = FigureCanvasTkAgg(self.fig, master=self.frame)
		self.canvas_widget = self.canvas.get_tk_widget()
		self.canvas_widget.pack(fill="both", expand=True)#.grid(row=self.row, column=self.column)

		# create the animation using figure and update method
		self.animation = FuncAnimation(self.fig, self.update, interval=self.t_k * 1000)

	def stop(self):
		"""
		Stops the updating of the array / time by adjusting the collecting_data variable.
		"""

		self.collecting_data = False

	def start(self):
		"""
		Starts the updating of the array / time by adjusting the collecting_data variable.
		"""

		self.collecting_data = True

	def reset(self):
		"""
		Resets arrays to initial values and starts collection.
		"""

		# initialise time and storing arrays
		self.ts = np.array([0])
		self.hs = np.array([self.h(0)])

		# whether we want to collect data initially
		self.collecting_data = True

	def save(self, filename):
		"""
		Saves the figure according to the filename (extension must be included).
		"""

		self.fig.savefig(filename, bbox_inches="tight")

	def toggle_grid(self):
		"""
		Toggles the use_grid boolean.
		"""

		self.use_grid = not self.use_grid

	def set_title(self, title):
		"""
		Sets the title of the figure to the given string.
		"""

		self.fig.suptitle(title)