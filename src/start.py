import pygame
from src.button import button
white = (255, 255, 255)
black = (0, 0, 0)
green = (34, 177, 76)
lightgreen = (0, 255, 0)
blue = (0, 0, 255)


class start:

	def __init__(self, surface, x, y, screenwidth = 740, screenheight = 580, inactivecolor, activecolor, action = None):
		"""
		this funtion initializes start screen characteristics
		args: surface:(object); x:(int, x coordinate); y:(int, y coordinate); screenwidth:(int, width of screen); screenheight(int, height of screen); inactivecolor:(inactive color); activecolor:(active color); action: (bool, action done to button)
		return: none
		"""
		self.surface = surface
		self.x = x
		self.y = y
		self.height = screenheight
		self.width = screenwidth
		self.acolor = activecolor
		self.icolor = inactivecolor
		self.action = action
	

	def startScreen(self):
		"""
		this funtions creates the start screen, displays the title and the start button
		args: none
		returns: none
		"""
		pygame.init()
		#sets up screen
		surface = pygame.display.set_mode((self.width, self.height))
		#displays button	
		button1 = button(self.surface, self.x, self.y, 100, 60, green, lightgreen, action = "play")
	
		pygame.draw.rect(surface, green, pygame.Rect(330, 400, 100, 60))
		pygame.display.flip()
		game_over = False
		while not game_over:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
			button1.hoverbutton()
			font = pygame.font.SysFont(None, 24)
			txt = font.render('PLAY', True, black)
			surface.blit(txt, (340, 419))
			pygame.display.flip()


			#gametitle
			font = pygame.font.SysFont(None, 24)
			txt = font.render('SWIMMY FISH', True, blue)
			surface.blit(txt, (200, 100))
			pygame.display.flip()
