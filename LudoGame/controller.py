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

import random
from views import Board
from models import TRACK, OVALS, TEAM, F_TRACK


# Frame Of Dice Function
class Dice(Tkinter.Frame):
	def __init__(self,root, s):
		Tkinter.Frame.__init__(self,root)
		self.string = s
		self.string.set(6)
		self.create_widget()
	#
	def round(self):
		self.string.set(random.randint(1,6))
		self.button.config(state="disable")
		return

	def create_widget(self):
		store = Tkinter.Label(self, textvariable=self.string,width=20)
		store.pack(fill='both')
		self.button = Tkinter.Button(self, text="Team A", command=self.round)
		self.button.pack(fill='both')
		return




# Frame Of ScoreBoard
class ScoreBoard(Tkinter.LabelFrame):
	def __init__(self, *args, **kwargs):
		Tkinter.LabelFrame.__init__(self, *args, **kwargs)
		self['padx']=20
		self['pady']=20
		self.create_label()

	# Creating Label
	def create_label(self):
		Tkinter.Label(self, text="Team A", bg="RoyalBlue1").grid(row=1, column=1)
		Tkinter.Label(self, text="Team B", bg="yellow2").grid(row=2, column=1)
		self.team_a=Tkinter.Label(self, text="0")
		self.team_a.grid(row=1, column=2)
		self.team_b=Tkinter.Label(self, text="0")
		self.team_b.grid(row=2, column=2)
		return




# Creating Main Engine 
class Engine:
	def __init__(self, canvas):
		self.canvas = canvas
		#self.ovals=[]
		self.create_ovals()
		self.turn = "A"
		self.number = Tkinter.IntVar()
		self.add_dice()
		self.score_board()


	# Add Dice Frame
	def add_dice(self):
		self.dice=Dice(self.canvas.master, self.number)
		self.dice.pack(side='left')
		return


	#Add Score Board
	def score_board(self):
		self.score=ScoreBoard(self.canvas.master, text="Score")
		self.score.pack(side='right')
		return

	# Creating Ovals
	def create_ovals(self):
		self.oval_identity=[]
		for a,b,c,d in OVALS:
			for i in b:
				s=self.canvas.create_oval(*self.getcoordinates(i), fill=c, tag="C{}".format(i), activewidth=3)
				self.oval_identity.append("C{}".format(i))
				self.canvas.tag_bind(s, "<Button-1>", self.oval_triggers)
		
		return

	
	# Oval Binding Handler
	def oval_triggers(self, event):
		tag = self.selected_oval(event)
		if tag and (self.number.get()!=0):
			# Team A
			if self.turn =="A":
				if tag in TEAM[0]:
					
					# TEAM A PLAYERS
					self.team_a_moves(tag)


			# Team B
			else:
				if tag in TEAM[1]:
					
					# TEAM B PLAYERS
					self.team_b_moves(tag)
		return


	# Uplifting Ovals
	def uplifting(self, team):
		for a,b,c,d in OVALS:
			# a = Track
			# b = Station
			# c = Color
			# d = Team
			for s in b:
				tag=str("C"+s)
				if (d==team) and tag:
					# uplift here
					self.canvas.lift(tag)
		return

	# Team A Moves
	def team_a_moves(self, tag):
		for a,b,c,d in OVALS:
			# a = Track
			# b = Station
			# c = Color
			# d = Team
			for s in b:
				if str("C"+s)==tag:
					step=self.number.get()

					# Open
					if (step==1 or step==6) and not self.gettrackbox(tag):
						self.change_place(tag,a[0])
						print "Change Place to Start"
					
					else:
						print "Check"
						# In Track
						
						t = self.gettrackbox(tag)
						if t:
							present_address = a.index(t)
							print t, a[-2]
							if t==a[-2]:
								self.score.team_a.config(text=str(int(self.score.team_a.cget("text"))+1))
								self.canvas.delete(tag)
							try:
								self.change_place(tag,a[present_address+step])
								#self.check_turns()
							except:
								pass
							t = self.gettrackbox(tag)
							if t==a[-2]:
								print "One Coin Clear"
								# One Coin Clear
								self.canvas.delete(tag)
						else:
							self.check_turns()
					return
		return 


	# Team B Moves
	def team_b_moves(self, tag):
		for a,b,c,d in OVALS:
			# a = Track
			# b = Station
			# c = Color
			# d = Team
			for s in b:
				if str("C"+s)==tag:
					step=self.number.get()

					# Open
					if (step==1 or step==6) and not self.gettrackbox(tag):
						self.change_place(tag,a[0])
						print "Change Place to Start"
					
					else:
						print "Check"
						# In Track
						
						t = self.gettrackbox(tag)
						if t:
							present_address = a.index(t)
							print t, a[-2]
							if t==a[-2]:
								self.score.team_b.config(text=str(int(self.score.team_a.cget("text"))+1))
								self.canvas.delete(tag)
							try:
								self.change_place(tag,a[present_address+step])
								#self.check_turns()
							except:
								pass
							t = self.gettrackbox(tag)
							if t==a[-2]:
								print "One Coin Clear"
								# One Coin Clear
								self.canvas.delete(tag)
						else:
							self.check_turns()
				
					return
				else:
					print "not selected"
		return 

	# Shape Movement Handler
	def change_place(self, tag, track):
		a,b,c,d=self.getcoordinates(tag)
		e,f,g,h=self.getcoordinates(track)
		self.canvas.move(tag, g-c, h-d)
		self.check_turns()

		return

	# Get Square Shape Tag on Which Coin Shape Is Lying
	def gettrackbox(self, tag):
		for i in TRACK:
			if self.getcoordinates(i)==self.getcoordinates(tag):
				return i
		for l in F_TRACK:
			for i in l:
				if self.getcoordinates(i)==self.getcoordinates(tag):
					return i
		return 

	# Selected Oval Tag Return
	def selected_oval(self, event=None):
		x , y = event.x, event.y
		for i in self.oval_identity:
			x1,y1,x2,y2 = self.getcoordinates(i)
			if (x1<=x) and (x<=x2) and (y1<=y) and (y<=y2):
				return i

	# Team Turn handlers
	def check_turns(self):
		self.dice.button.config(state="normal")
		self.number.set(0)
		if self.turn == "A":
			self.turn = "B"
			self.dice.button.config(text="Team B")
			self.uplifting("B")
			return 
		else:
			self.turn = "A"
			self.dice.button.config(text="Team A")
			self.uplifting("A")
			return 

	# Get Tag Coordinates In Canvas
	def getcoordinates(self, tags):
		return self.canvas.coords(tags)




# Main Trigger
if __name__=="__main__":
	root=Tkinter.Tk()
	d=Board(root)
	d.pack()
	e=Engine(d)
	root.mainloop()
