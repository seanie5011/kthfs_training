import customtkinter as ctk
from settings import *
from functools import partial

class SidePanel(ctk.CTkFrame):
	"""
	Contains the input widgets at the bottom of the window.
	"""

	def __init__(self, parent, animation):
		# can give the frames properties here
		super().__init__(master=parent, fg_color=INPUT_BG_COLOR, corner_radius=0)

		# WIDGETS

		# buttons to start, stop and reset the animation
		# placed at bottom right
		ctk.CTkButton(self, text="SAVE PNG", command=partial(animation.save, "thisfile.png")).grid(row=0, column=0, padx=(40, 0), pady=(100, 20))
		ctk.CTkButton(self, text="SAVE PDF", command=partial(animation.save, "thisfile.pdf")).grid(row=1, column=0, padx=(40, 0), pady=20)
		ctk.CTkButton(self, text="SAVE SVG", command=partial(animation.save, "thisfile.svg")).grid(row=2, column=0, padx=(40, 0), pady=20)