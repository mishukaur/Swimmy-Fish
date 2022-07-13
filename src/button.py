import pygame 

BLACK = (0, 0, 0)
GREEN = (34, 177, 76)
LIGHTGREEN = (0, 255, 0)
RED = (200, 0, 0)
LIGHTRED = (255, 0, 0)

class button:



	def __init__(self, surface, x, y, width, height, inactivecolor, activecolor, action = None):
		"""
		this function initializes all the parameters used for the button class
		args: surface:(object); x:(int, x coordinate); y:(int, y coordinate); screenwidth:(int, width of screen); screenheight(int, height of screen); inactivecolor:(inactive color); activecolor:(active color); action: (bool, action done to button)
		retuns: none
		"""
		black = (0, 0, 0)
		self.surface = surface
		self.x = x
		self.y = y
		self.height = height
		self.width = width
		self.acolor = activecolor
		self.icolor = inactivecolor
		self.action = action

	def labelbutton(self):
		"""
		this function labels the button
		args: none
		return: none
		"""
		font = pygame.font.SysFont(None, 24)
		txt = font.render(self.action, True, BLACK)
		self.surface.blit(txt, (self.x, self.y))


	def hoverbutton(self, cur, click):
		'''
		this function highlights the button when it's been hovered over and 
		args:self, cur(the position of the cursor), click(when the mouse is clicked)
		returns: pressed(bool)
		'''
		pressed = False
		pygame.draw.rect(self.surface, self.icolor, pygame.Rect(self.x, self.y, self.width, self.height)) 
		
		if (self.x + self.width) > cur[0] > self.x and (self.y + self.height) > cur[1] > self.y:
			pygame.draw.rect (self.surface, self.acolor, pygame.Rect(self.x, self.y, self.width, self.height))
			if click [0] == 1 and self.action != None:
				pressed = True
		else:
			pygame.draw.rect (self.surface, self.icolor, pygame.Rect(self.x, self.y, self.width, self.height))
		self.labelbutton()
		return pressed
