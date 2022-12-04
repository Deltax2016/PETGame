import sys, pygame
from game import *
import random
pygame.init()

sz = 8

global_width = 90
global_height = 90

Map, rooms = createDungeon(global_width,global_height,3)

#finalMap = createBox(global_width,global_height, Map)

size = [global_width*sz, global_height*sz]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Example code for the draw module")
done = False
clock = pygame.time.Clock()

colors = []

for n in range(len(rooms)):
	r = random.randint(0,255)
	g = random.randint(0,255)
	b = random.randint(0,255)
	colors.append((r,g,b))

while not done:

	clock.tick(60)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			print(event.type)
			done = True

	screen.fill("black")

	'''
	for i in range(0,len(finalMap)):
		for j in range(0,len(finalMap[i])):
			if finalMap[i][j] != ' ':
				pygame.draw.rect(screen, "green", [j*sz,i*sz,sz,sz], 3)
	'''
	cnt = 0
	for i in rooms:
		pygame.draw.rect(screen, colors[cnt], [i[2]*sz,i[3]*sz,(i[0]-i[2])*sz,(i[1]-i[3])*sz])
		cnt += 1


	pygame.display.flip()

# Be IDLE friendly
pygame.quit()
