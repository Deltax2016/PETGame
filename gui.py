import sys, pygame
from game import *
pygame.init()

sz = 8

global_width = 100
global_height = 100

Map = createDungeon(global_width,global_height,4)

finalMap = createBox(global_width,global_height, Map)

size = [global_width*sz, global_height*sz]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Example code for the draw module")
done = False
clock = pygame.time.Clock()

while not done:

	clock.tick(60)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			print(event.type)
			done = True

	screen.fill("black")

	for i in range(0,len(finalMap)):
		for j in range(0,len(finalMap[i])):
			if finalMap[i][j] != ' ':
				pygame.draw.rect(screen, "green", [j*sz,i*sz,sz,sz], 3)


	pygame.display.flip()

# Be IDLE friendly
pygame.quit()
