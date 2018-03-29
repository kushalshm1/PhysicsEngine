import vectorOperationLibrary as v 
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

#Vectors:

positionVector = (v.create('positionVector',500/2,500/2))
velocityVector = v.create('velocityVector',10,10)
accelerationVector = v.create('accelerationVector',0,100)
# v.setAngle(accelerationVector,math.pi/4)
print(accelerationVector)
position = [0]*2 


#Initialising Pygame
pg.init()
radius = 300
displayDimensions = [500,500]
mainDisplay = pg.display.set_mode(displayDimensions)
speed = 0
#Update Function
def update():
	global radius,positionVector,velocityVector,position,speed,accelerationVector
	mainDisplay.fill(red)
	position = v.add(positionVector,velocityVector)
	position = v.add(position,accelerationVector)
	position = v.multiplyScalar(position,speed)
	position = v.toInt(v.multiplyScalar(position,speed))
	speed = speed+0.001
	position = list(position)
	if(position[0]+radius>500):
		accelerationVector = [0,0]
		velocityVector[0] = (-1)*velocityVector[0]
	if(position[1]+radius>500):
		velocityVector[1] = (-1)*velocityVector[1]
		accelerationVector = [0,0]

	print(position)
	pg.draw.circle(mainDisplay,white,position,(radius/16),0)









	pg.display.update()



#Main Loop
while True:
	for event in pg.event.get():
		if(event.type == pg.QUIT):
			pg.quit()
			sys.exit()
	
	update()