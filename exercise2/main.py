import customtkinter as ctk
from settings import *
from plot_realtime import RealtimePlotting
from input import InputPanel

# set to dark appearance mode
# to use system default, set to 'system'
ctk.set_appearance_mode("dark")

class App(ctk.CTk):
	"""
	Contains the window for the app.
	"""
	def __init__(self):
		# initialise with foreground color
		super().__init__(fg_color=BG_COLOR)

		# define the window properties

		self.title("")
		self.geometry("900x800")

		self.protocol("WM_DELETE_WINDOW", self.quit)

		# create the plotting frames

		self.frame1 = ctk.CTkFrame(self)
		self.frame1.pack(fill="both", expand=True)
		self.animation1 = RealtimePlotting(self.frame1)

		self.frame2 = ctk.CTkFrame(self)
		self.frame2.pack(fill="both", expand=True)
		self.animation2 = RealtimePlotting(self.frame2)

		# the input panel
		InputPanel(self, self.animation1)

		# call main loop to run
		self.mainloop()

if __name__ == "__main__":
    App()