#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Written By:
#		S.S.B
#		surajsinghbisht054@gmail.com
#		bitforestinfo.blogspot.com
#
#	
#
#
##################################################
######## Please Don't Remove Author Name #########
############### Thanks ###########################
##################################################
#
#
# Import Module
try:
	import Tkinter
except:
	import tkinter as Tkinter

from GameConfig import *
from models import *




# Main Class For Canvas Widget
class Board(Tkinter.Canvas):
	def __init__(self, *args, **kwargs):
		Tkinter.Canvas.__init__(self, *args, **kwargs)
		self.create_squares()
		self.highlight()
		self.configure(width=S_WIDTH*AREA, height=S_HEIGHT*AREA)


	# Filling Colors In Boxes
	def highlight(self):

		# Main Tracks
		for c in TRACK:
			self.itemconfigure(c, fill=C_0_D, activewidth=2, activefill=C_0_A, activeoutline="black")

		# Ending Tracks
		for n,k in enumerate(F_TRACK):
			for j in k:
				self.itemconfigure(j, fill=COLOR[n], activewidth=2, activeoutline='black')


		# Stations
		for n,s in enumerate(STATIONS):
			for j,c in enumerate(s):
				self.itemconfigure(c, fill=COLOR[n], activewidth=2)
				coordinates = self.coords(c)
				#store=self.create_oval(*coordinates, fill=COLOR[n], width=3, tag="COIN{}{}".format(n,j))
				#self.tag_bind(store,"<Enter>",self.coin_bind)
#				print n,s,j,c
		
		# Stops
		for s in STOPS:
			self.itemconfigure(s, fill="gray58", activefill="gray70", activewidth=3, activeoutline="gray10")
		return

	# Creating Square Boxes
	def create_squares(self):
		for i in range(AREA):
			for j in range(AREA):
				self.create_rectangle(S_WIDTH*i, S_HEIGHT*j, (S_WIDTH*i)+S_WIDTH,(S_HEIGHT*j)+S_HEIGHT, tag="{}.{}".format(i,j), outline='white', fill="ivory")
#				self.create_text(S_WIDTH*i+20, S_HEIGHT*j+20, text="{}.{}".format(i,j))
		return


# main Trigger
if __name__=="__main__":
	root = Tkinter.Tk()
	c = Board(root, width=S_WIDTH*AREA, height=S_HEIGHT*AREA)
	c.pack(expand=True, fill="both")
	root.mainloop()
