import customtkinter as ctk
from settings import *
from plot_realtime import RealtimePlotting
from bottom import BottomPanel
from side import SidePanel
from functools import partial

# suppress warnings (RELEASE MODE)
import warnings
warnings.filterwarnings("ignore")

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

		self.title("Visualisation GUI")
		self.geometry("1440x810")

		self.protocol("WM_DELETE_WINDOW", self.quit)  # makes sure quits without errors
		self.resizable(False, False)  # not resizable

		# data to keep track of
		self.title_string = ctk.StringVar(value="")

		# 2 rows, 3 columns
		self.rowconfigure(0, weight=9)
		self.rowconfigure(1, weight=1)
		self.columnconfigure((0, 1), weight=1)

		# create the plotting frame

		self.frame1 = ctk.CTkFrame(self)
		self.frame1.grid(row=0, column=1, sticky="nsew")
		self.animation1 = RealtimePlotting(self.frame1, 0, 0, (8, 6), self.title_string.get())

		# the input panels

		BottomPanel(self, self.animation1, self.title_string).grid(row=1, column=1, sticky="nsew")

		SidePanel(self, self.animation1).grid(row=0, column=0, rowspan=2, sticky="nsew")

		# if user presses enter, then will change the title of the plot to the ctk string
		self.bind("<Return>", self.input_handler)

		# call main loop to run
		self.mainloop()

	def input_handler(self, event=None):
		"""
		Handles keyboard bindings.
		"""

		# if return binding is activated
		if event.keysym == "Return":
			self.animation1.set_title(self.title_string.get())

if __name__ == "__main__":
    App()