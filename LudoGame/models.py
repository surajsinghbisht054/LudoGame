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
from GameConfig import *


# Function For Track Coordinates Calculations
def tracks(s, r):
	return [s.format(i) for i in r]

# Creating Main Track Square Boxes
TRACK = []
TRACK+= tracks("6.{}", range(6))[::-1]
TRACK+= ['7.0']
TRACK+= tracks("8.{}", range(6))
TRACK+= tracks("{}.6", range(9,15))
TRACK+= ['14.7']
TRACK+= tracks("{}.8", range(9,15))[::-1]
TRACK+= tracks("8.{}", range(9,15))
TRACK+= ['7.14']
TRACK+= tracks("6.{}", range(9,15))[::-1]
TRACK+= tracks("{}.8", range(6))[::-1]
TRACK+= ['0.7']
TRACK+= tracks("{}.6", range(6))




# Creating Ending Tracks
F_TRACK=[]
F_TRACK.append(tracks("7.{}", range(1,7)))
F_TRACK.append(tracks("{}.7", range(8,14))[::-1])
F_TRACK.append(tracks("7.{}", range(8,14))[::-1])
F_TRACK.append(tracks("{}.7", range(1,7)))

# Now Creating Roots
TRAIN_1=TRACK[8:]+TRACK[:7]+F_TRACK[0]+['7.6']	 # ROOT One
TRAIN_2=TRACK[21:]+TRACK[:20]+F_TRACK[1]+['8.7'] # Root Two
TRAIN_3=TRACK[34:]+TRACK[:33]+F_TRACK[2]+['7.8'] # Root Three
TRAIN_4=TRACK[47:]+TRACK[:46]+F_TRACK[3]+['6.7'] # Root Four

# Station
STATIONS=[]
STATIONS.append(['11.2','12.2','11.3','12.3'])
STATIONS.append(['11.11','12.11','11.12','12.12'])
STATIONS.append(['2.11','3.11','2.12','3.12'])
STATIONS.append(['2.2','3.2','2.3','3.3'])

# TEAM A COINS
TEAM = []
TEAM.append(["C{}".format(i) for i in STATIONS[0]]+["C{}".format(i) for i in STATIONS[3]])
TEAM.append(["C{}".format(i) for i in STATIONS[1]]+["C{}".format(i) for i in STATIONS[2]])
#print TEAM

OVALS = [
(TRAIN_1, STATIONS[0], C_1, "A"),
(TRAIN_2, STATIONS[1], C_2, "B"),
(TRAIN_3, STATIONS[2], C_3, "B"),
(TRAIN_4, STATIONS[3], C_4, "A"),
]



# Stops
STOPS = [
'8.1',
'12.6',
'13.8',
'8.12',
'6.13',
'2.8',
'1.6',
'6.2',
]
