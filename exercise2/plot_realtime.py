import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import customtkinter as ctk

# set to dark appearance mode
# to use system default, set to 'system'
ctk.set_appearance_mode("dark")

# class to handle simulated realtime data and plotting
class RealtimePlotting():
	def __init__(self, frame):
		# ctk frame to be used
		self.frame = frame

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

		# initial plotting parameters and variables
		self.figure = plt.figure()
		self.line, = plt.plot(self.ts, self.hs)

		# start the plotting animation
		self.plot()

	def update(self, i):
		"""
		Called every frame of animation. Updates the figure and data if needed.
		"""

		# if we are collecting more data to plot
		if self.collecting_data:
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

		# set up the canvas to be given for ctk
		self.canvas = FigureCanvasTkAgg(self.figure, master=self.frame)
		self.canvas_widget = self.canvas.get_tk_widget()
		self.canvas_widget.pack(fill=ctk.BOTH, expand=True)

		# create the animation using figure and update method
		self.animation = FuncAnimation(self.figure, self.update, interval=self.t_k * 1000)

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

class App(ctk.CTk):
	'''
	Contains the window for the app.
	'''
	def __init__(self):
		# initialise with foreground color
		super().__init__()

		# WINDOW PROPERTIES

		self.title('')
		self.geometry('900x800')

		self.protocol("WM_DELETE_WINDOW", self.quit)

		self.frame1 = ctk.CTkFrame(self)
		self.frame1.pack(fill=ctk.BOTH, expand=True)
		self.animation1 = RealtimePlotting(self.frame1)

		self.frame2 = ctk.CTkFrame(self)
		self.frame2.pack(fill=ctk.BOTH, expand=True)
		self.animation2 = RealtimePlotting(self.frame2)

		# MAIN LOOP

		self.mainloop()

if __name__ == "__main__":
    App()