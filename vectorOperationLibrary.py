import math



def setX(vector,value):
	vector[0] = value
def setY(vector,value):
	vector[1] = value
def getX(vector):
	return vector[0]
def getY(vector):
	return vector[1]
def getLength(vector):
	return ()
def create(name,x,y):
	name =  [0,0]
	setX(name,x)
	setY(name,y)
	return name
def getLength(vector):
	return ((vector[0])**2+(vector[1]**2))**0.5

def setAngle(vector,angle):
	length = getLength(vector)
	vector[0] = math.cos(angle)*length
	vector[1] = math.sin(angle)*length

def getAngle(vector):
	return math.atan2(vector[1],vector[0])

def setLength(vector,length):
	angle = getAngle(vector)
	vector[0] = math.cos(angle) * length
	vector[1] = math.sin(angle) * length

def add(vector1,vector2):
	return [vector1[0]+vector2[0],vector1[1]+vector2[1]] 


def subtract(vector1,vector2):
	return [(vector1[0]-vector2[0]),(vector1[1]-vector2[1])] 
 


def multiplyScalar(vector,scalar):
	return [vector[0]*scalar,vector[1]*scalar]

def divideScalar(vector1,scalar):
	return [vector[0]/scalar,vector[1]/scalar]


def toInt(vector):
	return (int(vector[0]),int(vector[1]))