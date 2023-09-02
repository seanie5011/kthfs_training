import customtkinter as ctk
from settings import *

class InputPanel(ctk.CTkFrame):
	"""
	Contains the input widgets at the bottom of the window.
	"""

	def __init__(self, parent, animation):
		# can give the frames properties here
		super().__init__(master=parent, fg_color=INPUT_BG_COLOR, corner_radius=0)

		# display
		# fills to the left and right, and attaches to the bottom of the parent
		self.pack(fill="both", side="bottom")

		# WIDGETS

		# buttons to start, stop and reset the animation
		# placed at bottom right
		ctk.CTkButton(self, text="RESET", command=animation.reset).pack(side="right", padx=10, pady=10)
		ctk.CTkButton(self, text="STOP", command=animation.stop).pack(side="right", padx=10, pady=10)
		ctk.CTkButton(self, text="START", command=animation.start).pack(side="right", padx=10, pady=10)