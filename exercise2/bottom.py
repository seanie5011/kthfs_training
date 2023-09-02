import customtkinter as ctk
from settings import *

class BottomPanel(ctk.CTkFrame):
	"""
	Contains the input widgets at the bottom of the window.
	"""

	def __init__(self, parent, animation, title_string):
		# can give the frames properties here
		super().__init__(master=parent, fg_color=INPUT_BG_COLOR, corner_radius=0)

		# WIDGETS

		# button to toggle the grid
		# placed at bottom left
		ctk.CTkButton(self, text="TOGGLE GRID", command=animation.toggle_grid).grid(row=0, column=0, padx=(50, 10), pady=(15, 0))

		# the entry field for the title
		ctk.CTkEntry(
			self, 
			textvariable=title_string, 
			width=200, 
			placeholder_text="Enter title here and press RETURN",
			fg_color=BG_COLOR, 
			border_color=TEXT_COLOR, 
			border_width=1, 
		).grid(row=0, column=1, padx=(10, 300), pady=(15, 0))

		# buttons to start, stop and reset the animation
		# placed at bottom right
		ctk.CTkButton(self, text="START", command=animation.start).grid(row=0, column=2, padx=10, pady=(15, 0))
		ctk.CTkButton(self, text="STOP", command=animation.stop).grid(row=0, column=3, padx=10, pady=(15, 0))
		ctk.CTkButton(self, text="RESET", command=animation.reset).grid(row=0, column=4, padx=10, pady=(15, 0))