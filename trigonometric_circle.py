import pygame
import math

SCR_WIDTH = 220
SCR_HEIGHT = 480

RAD_SIZE = 100
CIRCLE_X = 105
CIRCLE_Y = 285
STD_FONT_SZ = 25
FREQUENCY = 0.05


def drawChart(FREQUENCY, time, turns, sin, cos, surface, font):
	"""Draws the FREQUENCY, time, distance, and sine and cosine values on the given surface"""

	freq_txt = font.render("Frequency: {:.3}Hz".format(FREQUENCY), False, (0,0,0))
	time_txt = font.render("Time: {:.3}s".format(time), False, (0,0,0))
	turn_txt = font.render("Turns: {:.3}".format(turns), False, (0,0,0))
	sin_txt = font.render("Sine: {:.3}".format(sin), False, (0,0,0))
	cos_txt = font.render("Cosine: {:.3}".format(cos), False, (0,0,0))

	surface.blit(time_txt,(0,0))
	surface.blit(freq_txt,(0,STD_FONT_SZ))
	surface.blit(sin_txt,(0,STD_FONT_SZ*2))
	surface.blit(cos_txt,(0,STD_FONT_SZ*3))
	surface.blit(turn_txt,(0,STD_FONT_SZ*4))


def drawCircle(x,y, surface, font):
	"""Draws the Trigonometry circle on the given surface in position x, y"""

	x_txt = font.render("x", False, (0,0,0))
	y_txt = font.render("y", False, (0,0,0))

	pygame.draw.line(surface,(0,0,0),(x-RAD_SIZE,y),(x+RAD_SIZE,y))  #x-axis  
	pygame.draw.line(surface,(0,0,0),(x,y-RAD_SIZE),(x,y+RAD_SIZE))  #y-axis
	pygame.draw.circle(surface,(0,0,0), (x,y), RAD_SIZE, 1) #main circle
	surface.blit(x_txt,(x+RAD_SIZE, y)) #x character
	surface.blit(y_txt,(x,y-RAD_SIZE-STD_FONT_SZ-4)) #y character


def main():
	pygame.init()
	pygame.display.set_caption("Trigonometric Circle v. 1.1")

	screen = pygame.display.set_mode((SCR_WIDTH, SCR_HEIGHT), 0, 32)
	font = pygame.font.SysFont("arial",STD_FONT_SZ)


	while True:

		screen.fill((255,255,255))


		time = pygame.time.get_ticks()/1000
		distance = 2*math.pi*time*FREQUENCY
		turns = time*FREQUENCY	
		cos = math.cos(distance)
		sin = math.sin(distance)

		#size of cosine and sine in pixels
		cos_pxl = int(cos*RAD_SIZE)
		sin_pxl = int(-sin*RAD_SIZE)


		##### Draw stuff in the screen
		drawChart(FREQUENCY, time, turns, sin, cos, screen, font)
		drawCircle(CIRCLE_X, CIRCLE_Y, screen, font)

		pygame.draw.circle(screen,(255,0,0), (CIRCLE_X+cos_pxl,CIRCLE_Y+sin_pxl), 5, 0) #dot

		#Auxiliary shapes
		pygame.draw.circle(screen,(255,0,0), (CIRCLE_X+cos_pxl,CIRCLE_Y), 3, 1) #cosine dot  
		pygame.draw.circle(screen,(255,0,0), (CIRCLE_X,CIRCLE_Y+sin_pxl), 3, 1) #sine dot	

		pygame.draw.line(screen,(255,0,0),(CIRCLE_X,CIRCLE_Y),(CIRCLE_X+cos_pxl,CIRCLE_Y), 2)  #projection in x (cos)
		pygame.draw.line(screen,(255,0,0),(CIRCLE_X,CIRCLE_Y),(CIRCLE_X,CIRCLE_Y+sin_pxl),2) #projection in y (sine)


		event = pygame.event.poll()
		if event.type == pygame.QUIT:
			break

		pygame.display.update()


	pygame.quit()

if __name__ == '__main__':
	main()
