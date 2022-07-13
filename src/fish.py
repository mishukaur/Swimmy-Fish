import pygame

class fish(pygame.sprite.Sprite):
	def __init__(self, name, x, y):
		"""
		initializes characteristic of fish
		args: (x): int, x value of transforming image; (y): int, y value of transforming image
		return: none
		"""
		pygame.sprite.Sprite.__init__(self)
		self.imagefile = "assets/swimmyfish fish.png"
		self.image = pygame.image.load(self.imagefile).convert_alpha()
		self.image = pygame.transform.scale(self.image, (100,100))
		self.mask = pygame.mask.from_surface(self.image)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.name = name
		self.speed = 1
	
	def moveUp(self):
		"""
		if not clicking, fish is moving down
		args: none
		return: none
		"""
		self.rect.y -= 50
	
	def update(self):
		"""
		updates fish as click
		args: none
		return: none
		"""
		self.rect.y += self.speed
