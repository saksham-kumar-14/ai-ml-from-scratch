import pygame
pygame.init()
WIDTH, HEIGHT = 1000,800
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Interactive linear regression")
playing = True

def main():
	global playing
	running = True
	data = []
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_q]:
				running = False
				playing = False
			elif pygame.key.get_pressed()[pygame.K_r]:
				running = False

		# displaying grid
		SCREEN.fill((255,255,255))
		pygame.draw.line(SCREEN, (0,0,0), (100,0), (100,HEIGHT), 1)
		pygame.draw.line(SCREEN, (0,0,0), (0,HEIGHT-100), (WIDTH,HEIGHT-100), 1)

		# get mouse pos
		pos = pygame.mouse.get_pos()
		if True in pygame.mouse.get_pressed() and 100<pos[0]<WIDTH and 0<pos[1]<HEIGHT-100 :
			print(pos)
			data.append(pos)	

		if len(data) > 1:
			x_total,y_total = 0,0

			# drawing data
			for i in data:
				pygame.draw.circle(SCREEN, (0,0,0), (i[0],i[1]), 5)
				x_total += i[0]
				y_total += i[1]

			x_mean = x_total/len(data)
			y_mean = y_total/len(data)

			num,den = 0,0
			for i in data:
				num += (i[0]-x_mean)*(i[1]-y_mean)
				den += (i[0]-x_mean)**2

			if den!=0:
				m = (num/den)
				b = y_mean - m*x_mean

				x1,x2 = 100,WIDTH
				y1 = m*x1 + b
				y2 = m*x2 + b
				pygame.draw.line(SCREEN, (255,0,0), (x1,y1), (x2,y2), 4)



		pygame.display.flip()

while playing:
    main()
pygame.quit()

