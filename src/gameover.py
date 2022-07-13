import pygame
from src.button import button
import time

white = (255, 255, 255)
black = (0, 0, 0)
green = (34, 177, 76)
lightgreen = (0, 255, 0)
red = (200, 0, 0)
lightred = (255, 0, 0)

class gameover():
	def __init__(self, surface, x, y, width = 740, height = 580, inactivecolor, activecolor, action = None):
		"""
		initializes gameover characteristics
		args: surface:(object); x:(int, x coordinate); y:(int, y coordinate); screenwidth:(int, width of screen); screenheight(int, height of screen); inactivecolor:(inactive color); activecolor:(active color); action: (bool, action done to button)
		return: none
		"""
		self.surface = surface
		self.x = x
		self.y = y
		self.height = height
		self.width = width
		self.acolor = activecolor
		self.icolor = inactivecolor
		self.action = action

	def gameoverScreen():
		pygame.init()
		#sets up screen
		surface = pygame.display.set_mode((740,580))
		#displays button	
		button1 = button(surface, 300, 300, 150, 60, green, lightgreen, action = "play again")
		pygame.draw.rect(surface, green, pygame.Rect(400, 400, 100, 60))
		pygame.display.flip()
		game_over = False
		while not game_over:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
			button1.hoverbutton()
			font = pygame.font.SysFont(None, 24)
			txt = font.render('PLAY AGAIN', True, black)
			surface.blit(txt, (340, 419))
			pygame.display.flip()

		button2 = button(surface, 330, 400, 150, 60, red, lightred, action = "quit")
		pygame.draw.rect(surface, red, pygame.Rect(400, 400, 100, 60))
		pygame.display.flip()
		game_over = False
		while not game_over:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
			button2.hoverbutton()
			font = pygame.font.SysFont(None, 24)
			txt = font.render('QUIT', True, black)
			surface.blit(txt, (340, 419))
			pygame.display.flip()

		#lose message
		font = pygame.font.SysFont(None, 24)
		txt = font.render('YOU LOSE', True, black)
		surface.blit(txt, (200, 100))




			pygame.display.flip()
