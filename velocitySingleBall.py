import vectorOperationLibrary as v 
import particleCreationLibrary as p
import pygame as pg 
import math 
import sys

#Defining Colors
black = (0,0,0)
blue = (0,0,155)
red = (155,0,0)
green = (0,155,0)
yellow = (255,0,255)
white = (255,255,255)

#Initialising Pygame
pg.init()
displayDimensions = [500,500]
mainDisplay = pg.display.set_mode(displayDimensions)


#All Variables and Vectors:
position = v.create('position',100,100)
velocity = v.create('velocity',1,1)

circleRadius = 30
#Update Function
def update():
	global circleRadius,position,velocity
	mainDisplay.fill(red)
	position = v.toInt(v.add(position,velocity))
	pg.draw.circle(mainDisplay,white,position,circleRadius,0)
	
	pg.display.update()



#Main Loop
while True:
	for event in pg.event.get():
		if(event.type == pg.QUIT):
			pg.quit()
			sys.exit()
	
	update()