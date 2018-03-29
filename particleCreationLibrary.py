import math
import vectorOperationLibrary as v 
position = [0]*2
velocity = [0]*2

def create(x,y,speed,direction):
	position = v.create('position',x,y)
	velocity = v.create('velocity',0,0)
	v.setLength(velocity,speed)
	v.setAngle(velocity,direction)
	return [position,velocity]


def addVelocity(self):
	return v.add(position,velocity)

print(create(2,3,5,5))
print(addVelocity())