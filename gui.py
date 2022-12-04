import sys, pygame
from game import *
import random
pygame.init()

sz = 8

global_width = 96
global_height = 96

Map, rooms = createDungeon(global_width,global_height,4)
finalMap = createHalfBox(global_width,global_height)

#finalMap = createBox(global_width,global_height, Map)

size = [global_width*sz, global_height*sz]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Dungeon")
done = False
clock = pygame.time.Clock()

colors = [[(0,0,254),(60,60,254)],[(128, 64, 48),(205,113,63)],[(128,128,128),(211,211,211)],[(221,160,221),(216,191,216)]]

'''

рандомайзер цветов

for n in range(len(rooms)):
	r = random.randint(0,255)
	g = random.randint(0,255)
	b = random.randint(0,255)
	colors.append((r,g,b))
'''

while not done:

	clock.tick(60)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			print(event.type)
			done = True

	screen.fill("black")


	''' 

	карта разделенная на сектора

	for i in range(0,len(finalMap)):
		for j in range(0,len(finalMap[i])):
			if finalMap[i][j] != ' ':
				pygame.draw.rect(screen, "green", [j*sz,i*sz,sz,sz], 3)
	'''
	cnt = 0
	for i in rooms:
		if i[0]-i[2] <= 3 or i[1]-i[3] <= 3:
			continue

		#pygame.draw.rect(screen, colors[i[4]][0], [i[2]*sz,i[3]*sz,(i[0]-i[2])*sz,(i[1]-i[3])*sz],2)
		
		for k in range(i[3],i[1]+1):
			for j in range(i[2],i[0]+1):
				if k == i[3] or k == i[1] or j == i[2] or j == i[0]:
					pygame.draw.rect(screen, colors[i[4]][0], [j*sz,k*sz,sz,sz])
				else:
					pygame.draw.rect(screen, colors[i[4]][1], [j*sz,k*sz,sz,sz])
		''' 

		дорожки между комнатами

		if i[0] < global_width-3:
			pygame.draw.rect(screen, 'white', [(i[0])*sz,(i[1]/2)*sz,sz*2,sz])
		if i[1] < global_height-3:
			pygame.draw.rect(screen, 'white', [(i[0]/2)*sz,(i[1])*sz,sz,sz*3])
		print(i[0]/2,i[1])
		'''
		cnt += 1


	pygame.display.flip()

# Be IDLE friendly
pygame.quit()
