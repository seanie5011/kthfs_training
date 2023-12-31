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
		ctk.CTkButton(self, text="SAVE PNG", command=partial(animation.save_image, ".png")).grid(row=0, column=0, padx=(40, 0), pady=(100, 20))
		ctk.CTkButton(self, text="SAVE PDF", command=partial(animation.save_image, ".pdf")).grid(row=1, column=0, padx=(40, 0), pady=20)
		ctk.CTkButton(self, text="SAVE SVG", command=partial(animation.save_image, ".svg")).grid(row=2, column=0, padx=(40, 0), pady=20)
		ctk.CTkButton(self, text="SAVE CSV", command=partial(animation.save_data, ".csv")).grid(row=3, column=0, padx=(40, 0), pady=20)

		# label for datapoints
		ctk.CTkLabel(self, text="Datapoints taken:").grid(row=4, column=0, padx=(40, 0), pady=(20, 5))
		ctk.CTkLabel(self, textvariable=animation.ts_str).grid(row=5, column=0, padx=(40, 0), pady=(5, 20))

		# label for period of data
		ctk.CTkLabel(self, text="Period (per unit time):").grid(row=6, column=0, padx=(40, 0), pady=(20, 5))
		ctk.CTkLabel(self, textvariable=animation.period_str).grid(row=7, column=0, padx=(40, 0), pady=(5, 20))

		ctk.CTkLabel(self, text="Amplitude:").grid(row=8, column=0, padx=(40, 0), pady=(20, 5))
		ctk.CTkLabel(self, textvariable=animation.amp_str).grid(row=9, column=0, padx=(40, 0), pady=(5, 20))