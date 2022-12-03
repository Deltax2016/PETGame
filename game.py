
import random

def createBox(_width, _height, _gameMap):	

	gameMap = _gameMap
	width = _width
	height = _height

	for i in range(0,height):
		for j in range(0,width):
			if not i or not j:
				gameMap[i][j] = '#'
			elif i == height - 1 or j == width - 1:
				gameMap[i][j] = '#'

	return gameMap


#Map = createBox(20, 10)
def createHalfBox(_width, _height, flag = 0):

	roomMap = []
	width = _width
	height = _height

	for i in range(0,height):
		line = []
		for j in range(0,width):
			line.append(' ')
		roomMap.append(line)

	return roomMap

def createHorizontalBox(_width, _height, boxMap, x, y, n):
	print('hor',_width, _height, x, y, n)
	gameMap = boxMap
	width = _width
	height = _height

	min_y = (n+1)**2 + y
	max_y = height - (n+1)**2
	a = random.randint(min_y,max_y)

	for i in gameMap[a]:
		for j in range(x,_width):
			if gameMap[a][j] == ' ':
				gameMap[a][j] = '*'

	if n > 1:
		gameMap = createVerticalBox(_width, a, boxMap, x, 0, n-1 )
		gameMap = createVerticalBox(_width, _height, boxMap, x, a, n-1)

	return gameMap

def createVerticalBox(_width, _height, boxMap, x, y, n):
	print('vert',_width, _height, x, y, n)
	gameMap = boxMap
	width = _width
	height = _height

	#print(2*n+x,width-2*n)
	min_x = (n+1)**2 + x
	max_x = width - (n+1)**2
	a = random.randint(min_x,max_x)

	for i in gameMap[y:height]:
		i[a] = '*'

	if n > 1:
		gameMap = createHorizontalBox(a, _height, boxMap, 0, y, n-1)
		gameMap = createHorizontalBox(_width, _height, boxMap, a, y, n-1)

	return gameMap


def createDungeon(_width, _height, _n):

	gameMap = []
	width = _width
	height = _height

	for i in range(0,height):
		line = []
		for j in range(0,width):
			line.append(' ')
		gameMap.append(line)

	gameMap = createVerticalBox(width, height, gameMap, 0, 0, _n)
	
	return gameMap

