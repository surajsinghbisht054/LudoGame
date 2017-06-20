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

from controller import Engine
from views import Board


if __name__ == '__main__':
	root=Tkinter.Tk()
	d=Board(root)
	d.pack()
	e=Engine(d)
	root.mainloop()