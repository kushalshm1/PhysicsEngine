import vectorOperationLibrary as v 
import pygame as pg 
import math 
import sys
import random
#Defining Colors
black = (0,0,0)
blue = (0,0,255)
red = (155,0,0)
green = (0,155,0)
yellow = (255,255,0)
white = (255,255,255)

#All Variables and Vectors:
numParticles = 100
position = []
velocity = []
acceleration = []
for x in range(0,numParticles):
	position.append(v.create('position',random.randint(0,numParticles),random.randint(0,numParticles)))
	velocity.append(v.create('velocity',random.randint(0,800),random.randint(0,600)))
	acceleration.append(v.create('acceleration',10,20))

colors = (black,green,red)
color = (0,0,0)

#Initialising Pygame
pg.init()
displayDimensions = [800,600]
mainDisplay = pg.display.set_mode(displayDimensions)




circleRadius = 1/10
earthRadius = 1
factor = 1
speed = 0
mainDisplay.fill(red)

#Update Function
def update():
	global circleRadius,position1,velocity,acceleration,position,speed,colors,color,earthRadius,factor
	pg.draw.circle(mainDisplay,yellow,[10,10],earthRadius,0)
	pg.draw.circle(mainDisplay,blue,[800/2,600/2],earthRadius,0)
	if(earthRadius>800/8):
		factor = 0
	earthRadius = earthRadius+factor

	for x in range(0,numParticles):
		position1 = v.add(position[x],velocity[x])
		position1 = v.add(position1,acceleration[x])
		position1 = v.multiplyScalar(position1,speed)
		position1 = v.toInt(position1)
		# color = colors[random.randint(0,2)]
		color =  yellow
		pg.draw.circle(mainDisplay,color,position1,circleRadius,0)

	speed = speed+0.001	
	pg.display.update()



# #Main Loop
while True:
	for event in pg.event.get():
		if(event.type == pg.QUIT):
			pg.quit()
			sys.exit()
	
	update()