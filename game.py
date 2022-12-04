
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
def createHalfBox(_width, _height):

	roomMap = []
	width = _width
	height = _height

	for i in range(0,height):
		line = []
		for j in range(0,width):
			line.append(' ')
		roomMap.append(line)

	return roomMap

def createHorizontalBox(_width, _height, boxMap, x, y, n, rooms):
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
		gameMap = createVerticalBox(_width, a, boxMap, x, y, n-1, rooms)
		gameMap = createVerticalBox(_width, _height, boxMap, x, a, n-1, rooms)
	else:
		r1 = random.randint(0,3)
		r2 = random.randint(0,3)
		rooms.append((_width, a, x, y,r1))
		rooms.append((_width, _height, x, a,r2))
	return gameMap, rooms

def createVerticalBox(_width, _height, boxMap, x, y, n, rooms):
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
		gameMap = createHorizontalBox(a, _height, boxMap, x, y, n-1, rooms)
		gameMap = createHorizontalBox(_width, _height, boxMap, a, y, n-1, rooms)
	else:
		r1 = random.randint(0,3)
		r2 = random.randint(0,3)
		rooms.append((a, _height, x, y,r1))
		rooms.append((_width, _height, a, y,r2))

	return gameMap, rooms


def createDungeon(_width, _height, _n):

	gameMap = []
	rooms = []
	width = _width
	height = _height

	for i in range(0,height):
		line = []
		for j in range(0,width):
			line.append(' ')
		gameMap.append(line)

	gameMap, rooms = createVerticalBox(width, height, gameMap, 0, 0, _n, rooms)

	#print(rooms)

	for cnt in range(len(rooms)):
		rooms[cnt] = (rooms[cnt][0] - 2, rooms[cnt][1] - 2, rooms[cnt][2] + 1, rooms[cnt][3] + 1, rooms[cnt][4])

	print(rooms)
	
	return gameMap, rooms


